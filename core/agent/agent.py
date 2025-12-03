from core.agent.document import Document
from core.agent.agent_schema import Schema
from core.agent.utils import parse_llm_json_block
from typing import List, Dict
from uuid import uuid1


class Agent:

    def __init__(
        self,
        schema: Schema = Schema(),
        agent_id=uuid1(),
        agent_name="agent",
        agent_prompt="",
        agent_type="gemini"
    ):
        self.schema = schema
        self.agent_id = agent_id
        self.agent_name = agent_name
        self.agent_prompt = agent_prompt
        self.agent_type = agent_type

    def __str__(self):
        return self.__dict__().__str__()

    def to_dict(self):
        return {
            "agent_schema": self.schema.__str__(),
            "agent_id": self.agent_id.__str__(),
            "agent_name": self.agent_name,
            "agent_type": self.agent_type,
            "agent_prompt": self.agent_prompt,
        }

    def query(self, data:str):
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

    def schema_induction(self, data:str) -> Dict:
        output = self.query( self.agent_prompt + " /n" + data)
        json_data = parse_llm_json_block(output)
        return json_data
    
    def schema_extraction(self, data:str) -> Dict:
        prompt = "you will be given a json file. Extract the schema"
        agent_query = f"{str(self.schema)} {prompt}"
        temp_stuff = self.query(agent_query)
        alt_json_data = parse_llm_json_block(temp_stuff)
        return alt_json_data
    


