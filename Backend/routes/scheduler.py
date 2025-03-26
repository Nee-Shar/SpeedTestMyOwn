from fastapi import APIRouter
from controller.scheduler import schedule_speed_test, cancel_scheduled_test, get_schedule_status

router = APIRouter()

@router.post("/schedule-speedtest/")
def schedule_speedtest(wait_time: int):
    # Schedules speed tests at fixed intervals.
    message = schedule_speed_test(wait_time)
    return {"message": message}

@router.get("/schedule-status/")
def check_schedule():
    # Returns the current schedule status.
    return get_schedule_status()

@router.delete("/cancel-schedule/")
def cancel_schedule():
    # Cancels the scheduled speed test.
    message = cancel_scheduled_test()
    return {"message": message}
