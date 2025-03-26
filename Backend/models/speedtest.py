from sqlalchemy import Column, Integer, Float, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
import datetime

Base = declarative_base()

class SpeedTestResult(Base):
    __tablename__ = "speed_test_results"

    id = Column(Integer, primary_key=True, index=True)
    download_speed = Column(Float, nullable=False)
    upload_speed = Column(Float, nullable=False)
    ping = Column(Float, nullable=False)
    server_used = Column(String, nullable=False)
    timestamp = Column(DateTime, default=datetime.datetime.utcnow)
