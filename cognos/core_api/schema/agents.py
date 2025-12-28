from typing import Dict, Literal, Any
from pydantic import BaseModel

class AgentCreateRequest(BaseModel):
    agent_name: str
    agent_type: Literal["openai", "gemini", "claude"]
    config: Dict[str, Any] = {}
