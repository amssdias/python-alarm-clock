# Alarm Clock with GUI

The objective of our project is to implement an alarm clock using Python. Python consists of some very innovative libraries such as datetime and tkinter which help us to build the project using the current date and time as well as to provide a user interface to set the alarm according to the requirement in 24-hour format.

## Pre requisites

- [Python](https://www.python.org/downloads/) - 3.8.4 or up

### Installing

- Download latest version of [Python](https://www.python.org/downloads/) :point_left:

  **1.** Go to the website above, and click on download

  **2.** Choose depending on which processor is your machine (in this example we looking to the files of Python 3.8.4)[Python](https://github.com/amssdias/PYTHON--School/blob/version1/img/python-download-versions.png)

  **3.** Double click and install (Add python to PATH just at the beginning of instalation)

### Run

- Download the project, open terminal window on folder with 'school.py' and type:

```
python alarm_clock.py
```

## Files

### alarm_clock.py

In this file I simple made the basic layout of the project

### alarm_func.py

In this file I have writted all the logic. There are only three functions:

```python
def set_alarm(hour, minute, frame_alarm)

def alarm_countdown(hour: int, minutes: int, label_time_missing)

def calc_time_missing(hour: int, minutes: int)
```

#### set_alarm:

In this function we get the entry from the user, and display the time missing.

#### alarm_countdown:

In this function we keep updating second by second how much time is missing.

#### calc_time_missing:

As the function name says, calculate the time missing.
