from flask import Flask
from api.routes.upload.upload_bp import upload_bp
from api.routes.agent.agent_bp import agent_bp

def create_app():
    app = Flask(__name__)
    app.register_blueprint(upload_bp)
    app.register_blueprint(agent_bp)
    return app
