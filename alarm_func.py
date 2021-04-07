from datetime import datetime, timedelta
import tkinter as tk


def set_alarm(hour, minute, frame_alarm, label_set, lbl_time_missing):

    # Get entry from user
    hour = int(hour.get())
    minutes = int(minute.get()) if minute.get() else 00
    frame_alarm.grid(row=2, column=0)
    label_set.pack_forget()

    if hour > 24:
        label_set['text'] = "Hour must be in 24 hour format. (00-23)"
        label_set.pack(side=tk.BOTTOM)
        return

    if minutes > 59:
        label_set['text'] = "Minute must be less than 60. (0-59)"
        label_set.pack(side=tk.BOTTOM)
        return

    label_set['text'] = f"Alarm is set to: {str(hour).zfill(2)}:{str(minutes).zfill(2)}"
    label_set.pack(side=tk.BOTTOM)

    # Calculate time missing
    time_missing = calc_time_missing(hour, minutes)

    lbl_time_missing['text'] = f"Time Missing: {time_missing}"
    lbl_time_missing.pack(side=tk.TOP)

    alarm_countdown(hour, minutes, lbl_time_missing)


def alarm_countdown(hour: int, minutes: int, label_time_missing):
    '''
    Update countdown clock
    '''
    # Check how much time is missing for the time entered
    time_missing = calc_time_missing(hour, minutes)
    label_time_missing['text'] = f"Time Missing: {time_missing}"

    if time_missing.total_seconds() == 0:
        label_time_missing['text'] = f"WAKE UP!"
        return

    # Repeat
    label_time_missing.after(1000, lambda: alarm_countdown(hour, minutes, label_time_missing))


def calc_time_missing(hour: int, minutes: int):
    '''
    Calculate time missing
    '''

    time = datetime.now()

    if time.hour > hour:
        # Calculate how much time missing to end the day
        time_to_end_of_day = timedelta(hours=24) - timedelta(hours=time.hour, minutes=time.minute, seconds=time.second)
        time_missing = time_to_end_of_day + timedelta(hours=hour, minutes=minutes)

    else:
        time_missing = timedelta(hours=hour, minutes=minutes) - \
        timedelta(hours=time.hour, minutes=time.minute, seconds=time.second)

    return time_missing