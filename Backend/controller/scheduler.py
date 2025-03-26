from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.interval import IntervalTrigger
from controller.speedtest import save_speed_test
from db import SessionLocal
from datetime import datetime

scheduler = BackgroundScheduler()
scheduler.start()
job_id = "speedtest_job"

def run_scheduled_speed_test():
   # Runs a speed test and saves results in the database.
    db = SessionLocal()
    try:
        save_speed_test(db)
        print(f"✅ [{datetime.now()}] Speed test saved.")
    except Exception as e:
        print(f"❌ Error running speed test: {e}")
    finally:
        db.close()

def schedule_speed_test(wait_time: int):
    # Schedules a recurring speed test at fixed intervals.
    global job_id
    if scheduler.get_job(job_id):  
        scheduler.remove_job(job_id)  # Remove old schedule if exists

    scheduler.add_job(
        run_scheduled_speed_test,
        trigger=IntervalTrigger(minutes=wait_time),
        id=job_id,
        replace_existing=True
    )
    return f"Speed test scheduled every {wait_time} minutes"

def cancel_scheduled_test():
   # Cancels the scheduled speed test.
    if scheduler.get_job(job_id):
        scheduler.remove_job(job_id)
        return "Speed test schedule canceled"
    return "No active schedule"

def get_schedule_status():
  # Returns the current schedule status.
    job = scheduler.get_job(job_id)
    if job:
        return {"status": "running", "next_run": str(job.next_run_time)}
    return {"status": "not running"}
