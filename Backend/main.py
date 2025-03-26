from fastapi import FastAPI
from routes.speedtest import router as speedtest_router
from routes.scheduler import router as scheduler_router
from models.speedtest import Base
from db import engine

app = FastAPI()

# Create tables on startup
Base.metadata.create_all(bind=engine)

# Register routes
app.include_router(speedtest_router)
app.include_router(scheduler_router)

@app.get("/")
def Home():
    return {"message": "💪🏽Speed Test API is running"}
