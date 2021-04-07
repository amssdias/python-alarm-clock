from datetime import datetime, timedelta
import tkinter as tk

from alarm_func import *

window = tk.Tk()

# Alarm layout
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

# Layout to set alarm
FRM_BTN = tk.Frame(master=window, pady=10)
FRM_BTN.grid(row=1, column=0)

BTN_SET_ALARM = tk.Button(
    master=FRM_BTN, 
    text="Set Alarm", 
    pady=10, 
    padx=8, 
    font=("Arial", 10),
    command=lambda: set_alarm(ENT_HOUR, ENT_MIN, FRM_ALARMED_SET, LBL_ALARMED_SET, LBL_TIME_MISSING))

BTN_SET_ALARM.grid(sticky="nsew")

# Layout to display time
FRM_ALARMED_SET = tk.Frame(master=window, pady=10)
LBL_ALARMED_SET = tk.Label(master=FRM_ALARMED_SET)
LBL_TIME_MISSING = tk.Label(master=FRM_ALARMED_SET)
    

window.mainloop()
