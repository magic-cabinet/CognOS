from document import Document
from agent_schema import Schema
from typing import List, Dict

class Agent:

    def ___init__(self, schema:Schema=None):
        self.schema = schema

    def explore(self, documents:List[Document]) -> Schema:
        """
        given an initial set of documents, those documents will generate
        the schema
        """
        pass

    def exploit(self, Schema, documents:List[Document])-> List[Dict]:
        """
        This is be used to generate a list of objects based on the schema
        """
        pass 