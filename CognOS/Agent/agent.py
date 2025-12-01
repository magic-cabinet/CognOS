from .document import Document
from .agent_schema import Schema
from CognOS.Agent.document import Document
from CognOS.Agent.agent_schema import Schema
from typing import List, Dict
from uuid import uuid1


class Agent:

    def __init__(
        self,
        schema: Schema = Schema(),
        agent_id=uuid1(),
        agent_name="agent",
        agent_prompt="",
    ):
        self.schema = schema
        self.agent_id = agent_id
        self.agent_name = agent_name
        self.agent_prompt = agent_prompt

    def __str__(self):
        return self.__dict__().__str__()

    def to_dict(self):
        return {
            "agent_schema": self.schema.__str__(),
            "agent_id": self.agent_id.__str__(),
            "agent_name": self.agent_name,
        }

    def query(self):
        pass

    def explore(self, documents: List[Document]) -> Schema:
        """
        given an initial set of documents, those documents will generate
        the schema
        """
        pass

    def exploit(self, Schema, documents: List[Document]) -> List[Dict]:
        """
        This is be used to generate a list of objects based on the schema
        """
        pass
