import os
from dotenv import load_dotenv
from typing import List, Optional
from pydantic import BaseModel, Field
from google import genai

load_dotenv()  # take environment variables

client = genai.Client(api_key=os.environ.get('GEMINI_API_KEY'))

class Ingredient(BaseModel):
    name: str = Field(description="Name of the ingredient.")
    quantity: str = Field(description="Quantity of the ingredient, including units.")

class Recipe(BaseModel):
    recipe_name: str = Field(description="The name of the recipe.")
    prep_time_minutes: Optional[int] = Field(description="Optional time in minutes to prepare the recipe.")
    ingredients: List[Ingredient]
    instructions: List[str]

####################################################################################################
### This is the output i got after asking claude to
### Generate the JSON Schema for Receipe `Recipe.model_json_schema()`
### LLMS being able to generate schemas will allow for tracable steps
### and emergent schemas given the context. 
###
### For example we can make an agent given the context generate a schema for other agents to use
### This schema is added to the prompt for the desrired output
###  and as of 1/17/2025 it ran successfully

### Generate schema, given an intial context, use the schema to extract data from other contexts
### The generated schemas simulate learning as if updates based on new contextes with respect
### to the pasts contexts it seen.
####################################################################################################

schema = """
{
    'properties': {
        'recipe_name': {
            'title': 'Recipe Name',
            'type': 'string'
        },
        'prep_time_minutes': {
            'anyOf': [{'type': 'integer'}, {'type': 'null'}],
            'title': 'Prep Time Minutes'
        },
        'ingredients': {
            'items': {
                'properties': {
                    'name': {
                        'title': 'Name',
                        'type': 'string'
                    },
                    'quantity': {
                        'title': 'Quantity',
                        'type': 'string'
                    }
                },
                'required': ['name', 'quantity'],
                'title': 'Ingredient',
                'type': 'object'
            },
            'title': 'Ingredients',
            'type': 'array'
        },
        'instructions': {
            'items': {'type': 'string'},
            'title': 'Instructions',
            'type': 'array'
        }
    },
    'required': ['recipe_name', 'ingredients', 'instructions'],
    'title': 'Recipe',
    'type': 'object'
}
"""



prompt = f"""
Please extract the recipe from the following text.
The user wants to make delicious chocolate chip cookies.
They need 2 and 1/4 cups of all-purpose flour, 1 teaspoon of baking soda,
1 teaspoon of salt, 1 cup of unsalted butter (softened), 3/4 cup of granulated sugar,
3/4 cup of packed brown sugar, 1 teaspoon of vanilla extract, and 2 large eggs.
For the best part, they'll need 2 cups of semisweet chocolate chips.
First, preheat the oven to 375°F (190°C). Then, in a small bowl, whisk together the flour,
baking soda, and salt. In a large bowl, cream together the butter, granulated sugar, and brown sugar
until light and fluffy. Beat in the vanilla and eggs, one at a time. Gradually beat in the dry
ingredients until just combined. Finally, stir in the chocolate chips. Drop by rounded tablespoons
onto ungreased baking sheets and bake for 9 to 11 minutes.

{schema}
"""

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=prompt,
    config={
        "response_mime_type": "application/json",
        # "response_json_schema": Recipe.model_json_schema(),
    },
)

recipe = Recipe.model_validate_json(response.text)
print(recipe)
x = 0