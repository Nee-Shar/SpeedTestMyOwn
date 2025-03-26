from sqlalchemy.orm import Session
from models.speedtest import SpeedTestResult
from schemas.speedtest import SpeedTestCreate
from controller.messages import send_telegram_message
import speedtest
import asyncio


def run_speed_test():
    #  Runs a speed test and returns results.
    st = speedtest.Speedtest()
    st.get_best_server()
    
    download_speed = st.download()
    upload_speed = st.upload()
    
    result = {
        "download_speed": round(download_speed / 1_000_000, 2),  # Convert to Mbps
        "upload_speed": round(upload_speed / 1_000_000, 2),
        "ping": round(st.results.ping, 2),
        "server_used": st.results.server["sponsor"] + " " + st.results.server["name"]


    }
    
    return result


def save_speed_test(db: Session):
    # Run speed test and save to DB
    result = run_speed_test()
    speedtest_entry = SpeedTestResult(**result)
    
    db.add(speedtest_entry)
    db.commit()
    db.refresh(speedtest_entry)

    message = (
        f"🚀 Speed Test Completed!\n\n\n"
        f"📡 Download: {result['download_speed']} Mbps\n"
        f"📤 Upload: {result['upload_speed']} Mbps\n"
        f"⚡ Ping: {result['ping']} ms\n"
        f"🌍 Server Used: {result['server_used']}\n"
        f"⏰ Timestamp:{result['timestamp']}"
    )
    send_telegram_message(message)
    return speedtest_entry

# def create_speed_test(db: Session, speedtest: SpeedTestCreate):
#     db_speedtest = SpeedTestResult(**speedtest.model_dump())  
#     db.add(db_speedtest)
#     db.commit()
#     db.refresh(db_speedtest)
#     return db_speedtest

def get_speedtests(db: Session, skip: int = 0, limit: int = 10):
    # Retrives stored speed test results
    return db.query(SpeedTestResult).offset(skip).limit(limit).all()
