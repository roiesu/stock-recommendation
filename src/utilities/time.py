from datetime import datetime, timedelta, timezone
from src.utilities.constants import DEV_MODE

def is_trading_hours():
    if DEV_MODE:
        return True
    now = datetime.now(timezone.utc)
    return now.weekday() < 5 and (
        (now.hour == 13 and now.minute >= 30) or (14 <= now.hour < 20)
    )

def get_data_interval():
    now = datetime.now(timezone.utc)
    minute = now.minute - (now.minute % 5)
    rounded_now = now.replace(minute=minute, second=0, microsecond=0)
    end = rounded_now - timedelta(minutes=15)
    start = end - timedelta(minutes=5)
    return start, end
