import tkinter as tk
from datetime import datetime, timezone

def set_alarm():
    # Get entry from user
    hour = int(ENT_HOUR.get())
    minute = int(ENT_MIN.get()) if ENT_MIN.get() else 00
    FRM_ALARMED_SET.grid(row=2, column=0)

    if hour > 24:
        LBL_ALARMED_SET['text'] = "Hour must be in 24 hour format. (00-23)"
        LBL_ALARMED_SET.pack(side=tk.BOTTOM)
        return

    if minute > 59:
        LBL_ALARMED_SET['text'] = "Minute must be less than 60. (0-59)"
        LBL_ALARMED_SET.pack(side=tk.BOTTOM)
        return

    LBL_ALARMED_SET['text'] = f"Alarm is set to: {hour}:{minute}"
    LBL_ALARMED_SET.pack(side=tk.BOTTOM)

    # Convert current time and alarmed time to minutes
    

    # time = datetime.now()
    # time_hour = str(abs(time.hour - hour)).zfill(2)
    # time_minute = str(abs(time.minute - minute)).zfill(2)

    LBL_TIME_MISSING = tk.Label(master=FRM_ALARMED_SET, text=f"Time Missing: {time_hour}:{time_minute}:{datetime.now().second}")
    LBL_TIME_MISSING.pack(side=tk.TOP)

    # alarm_countdown()
    

def alarm_countdown():
    # Check what time is it now
    today = datetime.now()
    time = today.time()

    # Check how much time is missing for the time entered
    LBL_TIME_MISSING['text'] = "something"

    # Repeat
    LBL_TIME_MISSING.after(1000, alarm_countdown)


window = tk.Tk()

# Frm choose hour
FRM_SET = tk.Frame(master=window)
FRM_SET.grid(row=0, column=0)
window.columnconfigure(0, minsize=250, weight=1)
window.rowconfigure(0, minsize=50, weight=1)

FRM_HOUR = tk.Frame(master=FRM_SET, padx=10, pady=20)
LBL_HOUR = tk.Label(master=FRM_HOUR, text="H:", padx=1)
ENT_HOUR = tk.Entry(master=FRM_HOUR, width=3)

FRM_MIN = tk.Frame(master=FRM_SET, padx=30, pady=20)
LBL_MIN = tk.Label(master=FRM_MIN, text="M:", padx=1)
ENT_MIN = tk.Entry(master=FRM_MIN, width=3)

FRM_HOUR.pack(side=tk.LEFT)
FRM_MIN.pack(side=tk.LEFT)
LBL_HOUR.pack(side=tk.LEFT, fill=tk.BOTH)
ENT_HOUR.pack(side=tk.LEFT, fill=tk.BOTH)
LBL_MIN.pack(side=tk.LEFT, fill=tk.BOTH)
ENT_MIN.pack(side=tk.LEFT, fill=tk.BOTH)


# Frm Button SET ALARM
FRM_BTN = tk.Frame(master=window, pady=10)
FRM_BTN.grid(row=1, column=0)

BTN_SET_ALARM = tk.Button(
    master=FRM_BTN, 
    text="Set Alarm", 
    pady=10, 
    padx=8, 
    font=("Arial", 10),
    command=set_alarm)

BTN_SET_ALARM.grid(sticky="nsew")


# Alarm setted
FRM_ALARMED_SET = tk.Frame(master=window, pady=10)
LBL_ALARMED_SET = tk.Label(master=FRM_ALARMED_SET, text="Your alarm is set to: ")


# lbl_clock = tk.Label(
#     master=frm_clock, 
#     text=datetime.now().strftime("%H:%M:%S"), 
#     font=("Arial", 50),
#     bg="black",
#     fg="white",
#     padx=20, pady=7)

# lbl_clock.pack(fill=tk.BOTH, expand=True)

# def timer():
#     lbl_clock['text'] = datetime.now().strftime("%H:%M:%S")

#     lbl_clock.after(1000, timer)

# timer()

window.mainloop()
