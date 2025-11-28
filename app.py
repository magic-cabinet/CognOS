from flask import Flask, jsonify, request
from CognOS.Agent.agent import Agent


app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({"message": "CognOS Flask app alive 🔥"})

@app.route("/create-agent")
def create_agent():
    temp_agent = Agent()
    return jsonify(temp_agent.to_dict())

@app.route("/echo", methods=["POST"])
def echo():
    data = request.json
    return jsonify({
        "received": data,
        "status": "ok"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
