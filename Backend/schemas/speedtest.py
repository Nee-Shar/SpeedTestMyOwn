from pydantic import BaseModel
from datetime import datetime

# Defines data structure for API REQ AND RES

class SpeedTestBase(BaseModel):
    download_speed: float
    upload_speed: float
    ping: float
    server_used: str


class SpeedTestCreate(SpeedTestBase):
    pass # used when adding a new speed test

class SpeedTestResponse(SpeedTestBase):
    id: int 
    timestamp: datetime

    class Config:
        from_attributes= True