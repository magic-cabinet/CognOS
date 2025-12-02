# CognOs
![CognOS Slime](/assets/cognos_slime_resized.png)

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
#### API Framework
FastAPI
#### Short Term Memory and Cache Managment
Redis
#### Long Term Memory
Supabase

### supported LLMs
- Anthropic
- Gemini
- OpenAI
- Ollama
- any llm that generates parsable json

## API

## Agents

### Create Your First Agent

```
curl -X POST http://localhost:8000/agent/create   -H "Content-Type: application/json"   -d '{
        "agent_name": "test",
        "agent_type": "gemini",
        "agent_prompt": "test prompt",
        "schema": {}
      }'
```

### List your Agents

```
curl -X GET http://localhost:8000/agent/
```

### Select An Agent 

```
curl -X GET http://localhost:8000/agent/<your-agent-id>
```

## Upload

### List upload

```
curl -X GET http://localhost:8000/upload/list
```

### Upload File

```
curl -X POST http://localhost:8000/upload/upload \
  -F "file=@./test.pdf" \
  -F "upload_as=my_custom_name.pdf"
```

### Get File

```
curl http://localhost:8000/upload/get/mydoc.pdf
```