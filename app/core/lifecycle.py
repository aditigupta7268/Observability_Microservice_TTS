from fastapi import FastAPI
import logging

def register_lifecycle_events(app: FastAPI):

    @app.on_event("startup")
    async def startup():
        logging.info("Service started")

    @app.on_event("shutdown")
    async def shutdown():
        logging.info("Graceful shutdown initiated")
