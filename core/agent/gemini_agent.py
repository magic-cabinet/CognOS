from typing import Optional, Dict, Any
from pydantic import BaseModel
from uuid import uuid1
from core.agent.agent import Agent
from core.agent.agent_schema import Schema
from dotenv import load_dotenv
import os
from google import genai

load_dotenv()

client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))


class GeminiAgent(Agent):

    def __init__(
        self,
        agent_schema: Schema = None,
        agent_id=None,
        agent_name: str = "gemini_agent",
        agent_prompt: str = "",
        model_version: str = "gemini-2.5-flash",
        agent_type: str = "gemini",
        agent_memory=None,
    ):
        if agent_schema is None:
            agent_schema = Schema()
        if agent_id is None:
            agent_id = uuid1()
        if agent_memory is None:
            agent_memory = []

        super().__init__(
            schema=agent_schema,
            agent_id=agent_id,
            agent_name=agent_name,
            agent_prompt=agent_prompt,
            # agent_type=agent_type
        )

        self.model_version: str = model_version
        # self.agent_memory = agent_memory

    def query(self, query: str):
        if query == "":
            query = "Explain how AI works in a few words"
        response = client.models.generate_content(
            model=self.model_version, contents=f"{self.agent_prompt} {query} memory:{self.agent_memory.__str__()}"
        )

        input_query = f"{self.agent_prompt} {query} memory:{self.agent_memory.__str__()}"

        # self.agent_memory.append(response.text)
        new_memory = {"memory_index": len(self.agent_memory),"user" : input_query, "agent_response": response.text }
        self.agent_memory.append(new_memory)

        return response.text
    

    def structured_output_query(self, query: str, model:BaseModel):
        if query == "":
            query = "Explain how AI works in a few words"
        response = client.models.generate_content(
            model=self.model_version, contents=f"{self.agent_prompt} {query} memory:{self.agent_memory.__str__()}",
                    config={
            "response_mime_type": "application/json",
            "response_schema": model,
        },
        )

        input_query = f"{self.agent_prompt} {query} memory:{self.agent_memory.__str__()}"

        # self.agent_memory.append(response.text)
        new_memory = {"memory_index": len(self.agent_memory),"user" : input_query, "agent_response": response.text }
        self.agent_memory.append(new_memory)

        return response.text
