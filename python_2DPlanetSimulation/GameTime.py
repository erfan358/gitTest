import datetime
import time

startTime = 0
delta_time = 0
previous_time = None  # Start as None to check initialization
Time = 0

def InitializeTime():
    global previous_time, startTime
    previous_time = datetime.datetime.now() 
    startTime = time.time()

def Calculate_DeltaTime():
    global previous_time, delta_time, Time, startTime  # ✅ Ensure global values are updated

    Time = time.time() - startTime
    current_time = datetime.datetime.now()

    if previous_time is None:  # ✅ Prevent errors if InitializeTime() wasn't called
        previous_time = current_time
        return 0 

    delta_time = (current_time - previous_time).total_seconds() 
    previous_time = current_time

    return delta_time
