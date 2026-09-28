from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from backend.agent.incident_agent import IncidentAgent
from backend.memory.hindsight_client import (
    initialize_memory,
    close_memory,
)


app = FastAPI(
    title="MemoryOps Incident Response Agent",
    description="AI incident response using Hindsight organizational memory",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class IncidentRequest(BaseModel):
    incident: str


agent = IncidentAgent()


@app.on_event("startup")
def startup_event():
    print("Initializing Hindsight...")
    initialize_memory()


@app.on_event("shutdown")
def shutdown_event():
    print("Closing Hindsight...")
    close_memory()


@app.get("/")
def root():
    return {
        "message": "MemoryOps Incident Response Agent is running"
    }


@app.post("/analyze")
def analyze_incident(request: IncidentRequest):

    result = agent.analyze(request.incident)

    return {
        "analysis": result["analysis"],
        "memories": result["memories"],
    }