from typing import Optional, Dict, Any
from uuid import uuid1
from CognOS.Agent.agent import Agent
from CognOS.Agent.agent_schema import Schema
from dotenv import load_dotenv
import os
from google import genai

load_dotenv()

client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))


class GeminiAgent(Agent):

    def __init__(
        self,
        schema: Schema = Schema(),
        agent_id=uuid1(),
        agent_name: str = "gemini_agent",
        agent_prompt: str = "",
        model_version: str = "gemini-pro",
        agent_type:str = "gemini",
    ):
        super().__init__(
            schema=schema,
            agent_id=agent_id,
            agent_name=agent_name,
            agent_prompt=agent_prompt,
            # agent_type=agent_type
        )

        self.model_version: str = model_version


    def query(self, query:str):
        if query == "":
            query = "Explain how AI works in a few words"
        response = client.models.generate_content(
            model="gemini-2.0-flash", contents=f"{self.agent_prompt} {query}"
        )

        return response.text
