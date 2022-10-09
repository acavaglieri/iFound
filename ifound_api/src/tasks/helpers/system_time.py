import os
import pytz
from datetime import datetime

def get_current_time():
    system_timezone = pytz.timezone(os.environ["SYSTEM_TIMEZONE"])
    current_time = datetime.now()
    current_time = system_timezone.localize(current_time)
    return current_time