import json
from core.agent.gemini_agent import GeminiAgent
from core.agent.utils import parse_llm_json_block


alt_temp_agent = GeminiAgent()
# temp_agent = GeminiAgent(agent_prompt="make your output a parsable json string")
# temp_agent = GeminiAgent(agent_prompt="make your output a json i need a output feild, reason feild, Entity List feild. DO NOT ADD ```python or ```json")
# temp_agent = GeminiAgent(agent_prompt="make your output a json i need a output feild, reason feild, Entity List feild.")

###############
## schema_induction
###############

temp_agent = GeminiAgent(agent_prompt="make your output a json i need a output feild, reason feild, Entity List feild consiting of entity and hypernym.")
data = temp_agent.query("")
json_data = parse_llm_json_block(data)

###############
## schema_extraction
###############

alt_agent_prompt = "you will be given a json file. Extract the schema"
alt_agent_query = f"{str(json_data)} {alt_agent_prompt}"
alt_data = alt_temp_agent.query(alt_agent_query)
alt_json_data = parse_llm_json_block(alt_data)
x = 0