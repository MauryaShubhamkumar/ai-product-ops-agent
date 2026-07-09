from pydantic import BaseModel

class AppResearch(BaseModel):
    app_name: str
    category: str
    description: str
    authentication: str
    self_serve: str
    api_surface: str
    graphQL: str
    mcp: str
    buildable: str
    blocker: str
    evidence: str
    confidence: int
