from contextlib import asynccontextmanager
from fastapi import FastAPI

# Routers
# from routers.agent_router import router as agent_router
# from routers.world_router import router as world_router
# from routers.health_router import router as health_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    print("🌍 CognOS API started")
    yield
    # Shutdown
    print("🛑 CognOS API shutting down")


def create_app() -> FastAPI:
    """
    CognOS FastAPI application factory.
    Keeps app construction clean and modular.
    """
    app = FastAPI(
        title="CognOS Engine",
        description="Agentic World Framework for Simulation, Reasoning, and Competitive Interaction",
        version="0.1.0",
        lifespan=lifespan,
    )

    # Register routers

    return app


# Create the application instance
app = create_app()


# Root route
@app.get("/")
def home():
    return {
        "message": "CognOS Engine alive 🔥",
        "status": "ok"
    }

