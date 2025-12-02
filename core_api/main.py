# from contextlib import asynccontextmanager
from fastapi import FastAPI
from core_api.lifespan import lifespan

# Routers
from core_api.routers.uploads import router as uploads_router
from core_api.routers.agents import router as agents_router

# from routers.world_router import router as world_router
# from routers.health_router import router as health_router




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
    app.include_router(agents_router, prefix="/agent", tags=["agents"])
    app.include_router(uploads_router, prefix="/upload", tags=["uploads"])

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

