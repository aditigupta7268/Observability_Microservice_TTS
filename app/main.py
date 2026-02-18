from fastapi import FastAPI
from app.core.config import settings
from app.middleware.observability import ObservabilityMiddleware
from app.api.routes import tts, health, monitoring
from app.core.lifecycle import register_lifecycle_events

def create_app() -> FastAPI:

    app = FastAPI(
        title=settings.app_name,
        version=settings.version
    )

    # Middleware
    app.add_middleware(ObservabilityMiddleware)

    # Routers
    app.include_router(tts.router)
    app.include_router(health.router)
    app.include_router(monitoring.router)

    register_lifecycle_events(app)

    return app

app = create_app()
