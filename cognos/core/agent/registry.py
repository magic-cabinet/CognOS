from typing import Dict, Type
from cognos.core.agent.agent import Agent
from cognos.core.agent.gemini_agent import GeminiAgent
# from cognos.core.agent.openai_agent import OpenAIAgent
# from cognos.core.agent.claude_agent import ClaudeAgent


AGENT_REGISTRY: Dict[str, Type[Agent]] = {
    "gemini": GeminiAgent,
    # "openai": OpenAIAgent,
    # "claude": ClaudeAgent,
}
