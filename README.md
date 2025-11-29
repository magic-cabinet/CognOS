# CognOs
![CognOS Slime](/asssets/cognos_slime_resized.png)

### Why we Built CognOs

```
"I intend, therefore i am"
```

This agent framework uses induced schema to simulate learning and generate agents with predictable, mutable and auditable behavior with the goal of alligning to the user.

Agents map spaces, sense spaces then extract information to make decisions.


### Running Docker Image

run 
```docker-compose up --build```

### Tech stack
- redis
- supabase
- flask

### supported LLMs
- Anthropic
- Gemini
- OpenAI
- Ollama
- any llm that generates parsable json

### Create Your First Agent

```
 curl -X POST http://localhost:8000/agent/create-agent   -H "Content-Type: application/json"   -d '{
    "schema": "whatever the user wants as a string",
    "agent_name": "MyAgent"
  }'
```
