import os
import json
import redis
from flask import Flask, jsonify, request
from api.app import create_app
from CognOS.Agent.agent import Agent
from CognOS.Agent.agent_schema import Schema
from typing import Optional, List, Dict
from api.routes.upload.upload_bp import upload_bp
from api.routes.agent.agent_bp import agent_bp

app = create_app()

@app.route("/")
def home():
    return jsonify({"message": "CognOS Flask app alive 🔥"})

@app.route("/echo", methods=["POST"])
def echo():
    data = request.json
    return jsonify({
        "received": data,
        "status": "ok"
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
