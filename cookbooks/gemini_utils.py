from google import genai
from os import environ
from dotenv import load_dotenv

load_dotenv()  # take environment variables
# userdata.get('GEMINI_API_KEY')
client = genai.Client(api_key=environ.get('GEMINI_API_KEY'))

response = client.models.generate_content(
    model="gemini-2.0-flash", contents="Explain how AI works in a few words"
)

print(response.text)