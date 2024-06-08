# Class/Meet Scheduler with Zoom Links

This Python script helps manage your online class schedule by opening Zoom links at specified times and announcing the start of each class using text-to-speech. 
Made this in lockdown when online classes era came into existence and I became way too much lazy to open links and remember timetable.
## Prerequisites

Make sure you have the following Python packages installed:

- `schedule`
- `pyttsx3`
- `webbrowser`

You can install these packages using pip:

```bash
pip install schedule pyttsx3
```

# How to Use
1. Save the Python script with a `.pyw` extension to run it without opening a command prompt window. For example, save it as scheduler.pyw.

2. Move the `.pyw` file to the following directory to run it automatically at startup:

```plaintext
C:\ProgramData\Microsoft\Windows\Start Menu\Programs\StartUp
```
3. Customize the script if needed. You can set the speaking speed, change the voice (male/female), and adjust the schedule according to your timetable.

# Script Explanation
The script is organized using a `ClassScheduler` class that handles scheduling, announcements, and opening Zoom links.

### ClassScheduler Class
- Initialization:
  - `__init__`: Initializes the text-to-speech engine and sets up the voice properties.
  - `setup_voice`: Configures the voice settings.
    
- Class Schedule Setup:
  - `create_schedule`: Defines the class schedules with messages and Zoom links.
    
-Scheduling Classes:

  - `schedule_classes`: Calls the scheduling functions for each class.
  - `schedule_daily`: Schedules classes that occur daily.
  - `schedule_weekly`: Schedules classes that occur on specific days of the week.

- Class Start:
  - `start_class`: Announces the class and opens the corresponding Zoom link.
    
- Running the Scheduler:

  - `run`: Starts the scheduling loop, checking for pending tasks every second.

# Running the Script
Run the script to start the scheduler. The script will announce the start of each class and open the corresponding Zoom link at the scheduled times. It runs in an infinite loop, checking the schedule every second.

```bash
python scheduler.pyw
```
 # Notes
- Ensure that your system volume is set appropriately to hear the announcements.
- Make sure your default web browser is set up properly to open Zoom links.
- You can modify the script to adjust the timings and Zoom links according to your own schedule.
