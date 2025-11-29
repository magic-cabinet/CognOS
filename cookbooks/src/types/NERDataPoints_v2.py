from pydantic import BaseModel
from enum import Enum

class DataType(Enum):
  ordinal = "ordinal"
  categorical = "categorical"



class Recipe(BaseModel):
    recipe_name: str
    ingredients: list[str]

class Entity(BaseModel):
    entity: str
    hpyernym: str
    data_type: DataType
    description: str
    verbs: 

class NERDataPoint(BaseModel):
    # text: str
    # entities: list[str]
    entities: list[Entity]