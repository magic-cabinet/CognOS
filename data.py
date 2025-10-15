from google import genai
from google import genai
from os import environ
from dotenv import load_dotenv

load_dotenv()  # take environment variables
# userdata.get('GEMINI_API_KEY')
client = genai.Client(api_key=environ.get('GEMINI_API_KEY'))
# from google.colab import userdata

MODEL_ID = "gemini-2.5-flash"  
     

directions = """
  To reach the Colosseum from Rome's Fiumicino Airport (FCO),
  your options are diverse. Take the Leonardo Express train from FCO
  to Termini Station, then hop on metro line A towards Battistini and
  alight at Colosseo station.
  Alternatively, hop on a direct bus, like the Terravision shuttle, from
  FCO to Termini, then walk a short distance to the Colosseum on
  Via dei Fori Imperiali.
  If you prefer a taxi, simply hail one at the airport and ask to be taken
  to the Colosseum. The taxi will likely take you through Via del Corso and
  Via dei Fori Imperiali.
  A private transfer service offers a direct ride from FCO to the Colosseum,
  bypassing the hustle of public transport.
  If you're feeling adventurous, consider taking the train from
  FCO to Ostiense station, then walking through the charming
  Trastevere neighborhood, crossing Ponte Palatino to reach the Colosseum,
  passing by the Tiber River and Via della Lungara.
  Remember to validate your tickets on the metro and buses,
  and be mindful of pickpockets, especially in crowded areas.
  No matter which route you choose, you're sure to be awed by the
  grandeur of the Colosseum.
"""
    
directions_prompt = f"""
  From the given text, extract the following entities and return a list of them.
  Entities to extract: street name, form of transport.
  Text: {directions}

  output it in parsable yaml
  Street = []
  Transport = []
"""

response = client.models.generate_content(
    model=MODEL_ID,
    contents=directions_prompt
)

print(response.text)
     