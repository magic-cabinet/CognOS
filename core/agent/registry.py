from typing import Dict, Type
from core.agent.agent import Agent
from core.agent.gemini_agent import GeminiAgent
# from core.agent.openai_agent import OpenAIAgent
# from core.agent.claude_agent import ClaudeAgent


AGENT_REGISTRY: Dict[str, Type[Agent]] = {
    "gemini": GeminiAgent,
    # "openai": OpenAIAgent,
    # "claude": ClaudeAgent,
}
