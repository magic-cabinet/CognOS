from flask import Flask, jsonify, request
from api.routes.upload.upload_bp import upload_bp
from api.routes.agent.agent_bp import agent_bp

def create_app():
    app = Flask(__name__)
    app.register_blueprint(upload_bp)
    app.register_blueprint(agent_bp)

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

    return app


