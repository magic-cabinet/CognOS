from typing import Optional, Dict, Any
from pydantic import BaseModel
from uuid import uuid1
from core.agent.agent import Agent
from core.agent.agent_schema import Schema
from core.agent.utils import download_image_bytes
from dotenv import load_dotenv
import os
from google import genai
from google.genai import types
import mimetypes
from urllib.parse import urlparse
from pathlib import Path


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
        response = client.models.generate_content(
            model=self.model_version, contents=f"{self.agent_prompt} {query} memory:{self.agent_memory.__str__()}"
        )

        input_query = f"{self.agent_prompt} {query} memory:{self.agent_memory.__str__()}"

        new_memory = {"memory_index": len(self.agent_memory),"user" : input_query, "agent_response": response.text }
        self.agent_memory.append(new_memory)

        return response.text
    

    def structured_output_query(self, query: str, model:BaseModel, file_path=[], urls=[]):

        part_list = []
        if file_path:
            for i in file_path:
                  with open(i, 'rb') as f:
                    image_bytes = f.read()
                    current_mime_types = mimetypes.guess_type(i)[0]

                    current_file_type = types.Part.from_bytes(
                        data=image_bytes,
                        mime_type=current_mime_types,
                        ),
                    part_list.extend(current_file_type)

        if urls:
            for i in urls:
                image_bytes = download_image_bytes(i)
                url_path = Path(urlparse(i).path)
                current_mime_types = mimetypes.guess_type(url_path)[0]

                current_file_type = types.Part.from_bytes(
                data=image_bytes,
                mime_type=current_mime_types,
                )
                part_list.append(current_file_type)


        response = client.models.generate_content(
            model=self.model_version, contents=[f"{self.agent_prompt} {query} memory:{self.agent_memory.__str__()}",part_list],
                    config={
            "response_mime_type": "application/json",
            "response_schema": model,
        },
        )

        input_query = f"{self.agent_prompt} {query} memory:{self.agent_memory.__str__()}"

        new_memory = {"memory_index": len(self.agent_memory),"user" : input_query, "agent_response": response.text }
        self.agent_memory.append(new_memory)

        return response.text
