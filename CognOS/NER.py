import os
from dotenv import load_dotenv
from google import genai
import json

load_dotenv()  # take environment variables

client = genai.Client(api_key=os.environ.get('GEMINI_API_KEY'))


sample = "{'properties': {'sentiment': {'enum': ['positive', 'neutral', 'negative'], 'title': 'Sentiment', 'type': 'string'}, 'summary': {'title': 'Summary', 'type': 'string'}}, 'required': ['sentiment', 'summary'], 'title': 'Feedback', 'type': 'object'}"

prompt = f"""
Describe the following text. generate a schema for similar documents you may see in the future

{sample}



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

"""

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=prompt,
    config={
        "response_mime_type": "application/json",
        # "response_json_schema": Recipe.model_json_schema(),
    },
)

# recipe = Recipe.model_validate_json(response.text)


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

{response.text}
"""

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=prompt,
    config={
        "response_mime_type": "application/json",
        # "response_json_schema": Recipe.model_json_schema(),
    },
)

# recipe = Recipe.model_validate_json(response.text)
output = json.loads(response.text)
print(output)
x = 0
