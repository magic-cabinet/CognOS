from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from core_api.services.redis_service import redis_service
from core.agent.agent import Agent
from core.agent.factory import build_agent
import json
from pydantic import Field
from typing import Optional, Dict, Any

router = APIRouter()


class AgentCreate(BaseModel):
    # schema: str = ""
    # agent_name: str = "agent"
    # agent_name="agent"
    # agent_prompt=""
    # agent_type="gemini"
    schema : str
    agent_name : str
    agent_name : str
    agent_prompt : str
    agent_type : str

class AgentResponse(BaseModel):
    agent_id: str
    agent_name: str
    schema: str

class CreateAgentRequest(BaseModel):
    agent_name: str = Field(..., description="Human-friendly name for the agent.")
    agent_type: str = Field(..., description="one of: gemini, openai, claude")
    agent_prompt: str = Field("", description="System / agent prompt.")
    schema: Optional[Dict[str, Any]] = Field(
        default=None, description="Initial schema (optional)"
    )
    config: Optional[Dict[str, Any]] = Field(
        default=None, description="Future model config (optional)"
    )

@router.get("/ping-redis")
async def ping_redis():
    await redis_service._client.set("hello", "world")
    value = await redis_service._client.get("hello")
    return {"redis": value}


@router.post("/create")
async def create_agent_route(body: CreateAgentRequest):
    try:
        agent = build_agent(
            agent_type=body.agent_type,
            agent_name=body.agent_name,
            agent_prompt=body.agent_prompt,
            schema=body.schema,
        )
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

    redis_key = f"agent:{agent.agent_id}"

    # MUST be awaited if Redis client is async
    await redis_service._client.set(redis_key, json.dumps(agent.to_dict()))

    return {
        "status": "success",
        "agent": agent.to_dict()
    }




@router.get("/")
async def list_agents() -> list[dict]:
    keys = await redis_service._client.keys("agent:*")   # async
    agents = []

    for key in keys:
        # key = key.decode()  # keys come back as bytes

        value = await redis_service._client.get(key)      # async

        if value:
            if isinstance(value, bytes):
                value = value.decode()

            agents.append(json.loads(value))

    return agents



@router.get("/{agent_id}")
async def get_agent(agent_id: str):
    agent_data = await redis_service._client.get(f"agent:{agent_id}")
    if not agent_data:
        raise HTTPException(404, "Agent not found")
    return json.loads(agent_data)

@router.get("/{agent_id}/schema-induction")
async def agent_schema(agent_id:str):
    agent_data = await redis_service._client.get(f"agent:{agent_id}")
    if not agent_data:
        raise HTTPException(404, "Agent not found")
    # json.loads(agent_data)

@router.delete("/{agent_id}", status_code=204)
async def delete_agent(agent_id: str):
    agent_data = await redis_service._client.get(f"agent:{agent_id}")
    if not agent_data:
        raise HTTPException(404, "Agent not found")
    await redis_service._client.delete(f"agent:{agent_id}")