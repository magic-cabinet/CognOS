from google import genai
from pydantic import BaseModel
from enum import Enum
import os
from dotenv import load_dotenv

load_dotenv()  # take environment variables
# userdata.get('GEMINI_API_KEY')
client = genai.Client(api_key=os.environ.get('GEMINI_API_KEY'))

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

class NERDataPoint(BaseModel):
    # text: str
    # entities: list[str]
    entities: list[Entity]




# client = genai.Client(api_key=userdata.get('GEMINI_API_KEY'))
response = client.models.generate_content(
    model="gemini-2.5-flash",
    # contents="List a few popular cookie recipes, and include the amounts of ingredients.",
    # contents="George Washington  was the first American president and bro was british. ",
    contents="George Washington  was the first American president and bro was british. The first PETase was discovered in 2016 from Ideonella sakaiensis strain 201-F6 bacteria found from sludge samples collected close to a Japanese PET bottle recycling site.[1][4] There were other types of hydrolases previously known to degrade PET,[2] including lipases, esterases, and cutinases.[5] For comparison, enzymes that degrade polyester have been known to exist at least as far back as 1975 (in the case of α-chymotrypsin)[6] and 1977 (lipase).[7]",
    config={
        "response_mime_type": "application/json",
        # "response_schema": list[Recipe],
        "response_schema": NERDataPoint,
    },
)
# Use the response as a JSON string.
print(response.text)

# Use instantiated objects.
# my_recipes: list[Recipe] = response.parsed
my_recipes: NERDataPoint = response.parsed
x = 0