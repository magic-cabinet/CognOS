import json
from flask import Blueprint, request, jsonify
from api.redis_client import get_redis_client, list_agents, get_agent_from_redis
from CognOS.Agent.agent import Agent

# agent_bp = Blueprint("agent", __name__)
agent_bp = Blueprint("agent", __name__, url_prefix="/agent")

@agent_bp.route("/ping-redis")
def ping_redis():
    get_redis_client().set("hello", "world")
    return {"redis": get_redis_client().get("hello")}

@agent_bp.route("/create-agent", methods=["POST"])
def create_agent():
    data = request.get_json(force=True)

    # Extract fields
    schema_str = data.get("schema", "")
    agent_name = data.get("agent_name", "agent")

    temp_agent = Agent(schema=schema_str, agent_name=agent_name)

    get_redis_client().set(f"agent:{temp_agent.agent_id}", json.dumps(temp_agent.to_dict()))

    # Return serialized agent
    return jsonify(temp_agent.to_dict())

@agent_bp.route("/get-agent/<agent_id>", methods=["GET"])
def get_agent(agent_id: str):
    agent = get_agent_from_redis(agent_id)
    if agent is None:
        return jsonify({"error": "Agent not found"}), 404
    return jsonify(agent.to_dict())

@agent_bp.route("/list-agents", methods=["GET"])
def list_agents_route():
    return jsonify(list_agents())
