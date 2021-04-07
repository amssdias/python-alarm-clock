import tkinter as tk
from datetime import datetime, timedelta


def set_alarm(hour, minute, frame_alarm):

    # Get entry from user
    hour = int(hour.get())
    minutes = int(minute.get()) if minute.get() else 00
    frame_alarm.grid(row=2, column=0)
    LBL_ALARMED_SET = tk.Label(master=frame_alarm, text="Your alarm is set to: ")

    if hour > 24:
        LBL_ALARMED_SET['text'] = "Hour must be in 24 hour format. (00-23)"
        LBL_ALARMED_SET.pack(side=tk.BOTTOM)
        return

    if minutes > 59:
        LBL_ALARMED_SET['text'] = "Minute must be less than 60. (0-59)"
        LBL_ALARMED_SET.pack(side=tk.BOTTOM)
        return

    LBL_ALARMED_SET['text'] = f"Alarm is set to: {str(hour).zfill(2)}:{str(minutes).zfill(2)}"
    LBL_ALARMED_SET.pack(side=tk.BOTTOM)

    # Calculate time missing
    time_missing = calc_time_missing(hour, minutes)

    LBL_TIME_MISSING = tk.Label(master=frame_alarm, text=f"Time Missing: {time_missing}")
    LBL_TIME_MISSING.pack(side=tk.TOP)

    alarm_countdown(hour, minutes, LBL_TIME_MISSING)


def alarm_countdown(hour: int, minutes: int, label_time_missing):
    '''
    Update countdown clock
    '''
    # Check how much time is missing for the time entered
    time_missing = calc_time_missing(hour, minutes)
    label_time_missing['text'] = f"Time Missing: {time_missing}"

    # Repeat
    label_time_missing.after(1000, lambda: alarm_countdown(hour, minutes, label_time_missing))


def calc_time_missing(hour: int, minutes: int):
    '''
    Calculate time missing
    '''

    time = datetime.now()
    if time.hour > hour:
        time_missing = timedelta(hours=time.hour, minutes=time.minute, seconds=time.second) - \
        timedelta(hours=hour, minutes=minutes)
    else:
        time_missing = timedelta(hours=hour, minutes=minutes) - \
        timedelta(hours=time.hour, minutes=time.minute, seconds=time.second)

    return time_missing