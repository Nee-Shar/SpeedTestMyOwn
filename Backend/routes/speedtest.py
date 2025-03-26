from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from controller.speedtest import  get_speedtests,save_speed_test
from schemas.speedtest import SpeedTestCreate,SpeedTestResponse
from db import get_db

router = APIRouter()

@router.get("/speedtest/", response_model=list[SpeedTestResponse])
def read_speedtests(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return get_speedtests(db, skip, limit)

# @router.post("/run",response_model=SpeedTestResponse)
# async def run_and_save_speedtest(db: Session=Depends(get_db)):
#     return await save_speed_test(db)
@router.post("/run", response_model=SpeedTestResponse)
def run_and_save_speedtest(db: Session = Depends(get_db)):
    return save_speed_test(db)
