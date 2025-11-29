import os
import json
import redis
from flask import Flask, jsonify, request
from CognOS.Agent.agent import Agent
from CognOS.Agent.agent_schema import Schema
from typing import Optional, List, Dict


AGENT_KEY_PREFIX = "agent:"

def get_redis_client() -> redis.Redis:
    return  redis.Redis(
        host=os.getenv("REDIS_HOST", "redis"),
        port=int(os.getenv("REDIS_PORT", "6379")),
        decode_responses=True
    )


def get_agent_from_redis(agent_id: str) -> Optional[Agent]:
    """
    Retrieve an Agent object from Redis using its agent_id.

    Args:
        agent_id (str): UUID of the agent.

    Returns:
        Optional[Agent]: The reconstructed Agent object if found,
                         otherwise None.
    """
    key = f"agent:{agent_id}"
    data = get_redis_client().get(key)

    if data is None:
        return None

    try:
        loaded = json.loads(data)
    except json.JSONDecodeError:
        return None

    # Rebuild Agent object
    return Agent(
        schema=loaded.get("schema", ""),
        agent_id=loaded.get("agent_id"),
        agent_name=loaded.get("agent_name", "agent")
    )


def list_agents() -> List[Dict]:
    """
    Return a list of all agent objects stored in Redis.
    """
    keys = get_redis_client().keys(f"{AGENT_KEY_PREFIX}*")
    agents = []
    for key in keys:
        raw = get_redis_client().get(key)
        if raw is None:
            continue
        try:
            agents.append(json.loads(raw))
        except json.JSONDecodeError:
            continue
    return agents