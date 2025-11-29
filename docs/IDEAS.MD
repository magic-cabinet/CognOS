- Add logging of agents actions for auditablity
- Allow for Agents to Listen to a address or get data, and react to aka post to a address
    - for example an endpoint could be an agent simulating Zork via a LLM

### Game
- A Game Object
    - game master agent
    - game turn List
    - ip address
    - list of agents listening
    - message to agents -> List[Agents]
    - listen for agent
    - timeout -> int seconds before agents counts inactive


### Agents
- copy agent