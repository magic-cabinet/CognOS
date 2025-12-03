import json
from uuid import UUID
from core.agent.registry import AGENT_REGISTRY
from core.agent.agent import Agent
from core.agent.gemini_agent import GeminiAgent


def agent_from_dict(data: dict) -> Agent:
    """
    Convert a saved dict back into the appropriate Agent subclass.
    """
    agent_type = data.get("agent_type", "").lower()

    if agent_type not in AGENT_REGISTRY:
        raise ValueError(f"Unknown agent_type: {agent_type}")

    AgentClass = AGENT_REGISTRY[agent_type]

    # Convert the types back (UUID, Schema, etc)
    agent_id = UUID(data["agent_id"])
    schema = str(data.get("schema", None))  # or reconstruct Schema if needed

    return AgentClass(
        agent_id=agent_id,
        agent_name=data["agent_name"],
        agent_prompt=data.get("agent_prompt", ""),
        schema=schema,
        agent_type=agent_type,
    )

def build_agent(agent_type: str, **kwargs) -> Agent:
    agent_type = agent_type.lower()

    if agent_type == "gemini":
        return GeminiAgent(**kwargs)
    # if agent_type == "openai":
    #     return OpenAIAgent(**kwargs)
    # if agent_type == "claude":
    #     return ClaudeAgent(**kwargs)

    raise ValueError(f"Unknown agent_type: {agent_type}")