# drivingTestProgram
Software developed for a simulated autonomous driving experiment. Built with PyQt6 and packaged with PyInstaller to be distributed to Windows computers.

## Tables of Contents
1. [Introduction](https://github.com/sf200212345/drivingTestProgram#introduction)
2. [TL;DR](https://github.com/sf200212345/drivingTestProgram#tldr)
3. [Using Autonomous_Driving_with_Tasks_Experiment (with example workflows)](https://github.com/sf200212345/drivingTestProgram#using-autonomous_driving_with_tasks_experiment)
3. [Notes on run_experiment (app_driver.py)](https://github.com/sf200212345/drivingTestProgram#notes-on-run_experiment)
    - [Instructions Page (/scripts/info_window.py)](https://github.com/sf200212345/drivingTestProgram#instructions-page)
    - [Experiment Page (/scripts/experiment_window.py)](https://github.com/sf200212345/drivingTestProgram#experiment-page)
    - [Survey Page (/scripts/survey_window.py)](https://github.com/sf200212345/drivingTestProgram#survey-page)
    - [Ending Page (/scripts/final_window.py)](https://github.com/sf200212345/drivingTestProgram#ending-page)
4. [Notes on settings (settings_driver.py)](https://github.com/sf200212345/drivingTestProgram#notes-on-settings)
    - [Storage Files](https://github.com/sf200212345/drivingTestProgram#storage-files)

## Introduction
This is a Python GUI built with the PyQt6 library containing an app GUI (app_driver.py) and a settings GUI (settings_driver.py). This was developed to conduct an experiment where participants would be prompted to watch a video simulating an autonomous driving experience. This video would have "emergency" situations built in, where a button would show up in the GUI at the same time an "emergency" situation occured in the video. Participants would have to press this, and their reaction times would be recorded. Participants would then be prompted to take a survey about their experience, and finally enter their participant ID for syncing data between the survey and reaction time data.

There are two modes available in the app: trivial and control. Control is exactly the app flow described above. Trivial is slightly different, as it also prompts participants to press a "I am paying attention" button while the video is playing to keep the participant engaged. This experiment therefore explores whether the addition of a "trivial" task helps the participant stay more engaged while in an autonomous driving experience.

## TL;DR

## Using Autonomous_Driving_with_Tasks_Experiment
Autonomous_Driving_with_Tasks_Experiment.zip will be the .zip file distributed, which contains the file structure listed:
```
Autonomous_Driving_with_Tasks_Experiment
├── run_experiment.exe
├── scripts
│   ├── __pycache__
│   │   ├── change_file_window.cpython-310.pyc
│   │   ├── experiment_window.cpython-310.pyc
│   │   ├── final_window.cpython-310.pyc
│   │   ├── info_window.cpython-310.pyc
│   │   ├── settings_styles.cpython-310.pyc
│   │   └── survey_window.cpython-310.pyc
│   ├── change_file_window.py
│   ├── experiment_window.py
│   ├── final_window.py
│   ├── info_window.py
│   └── survey_window.py
├── settings.exe
├── storage
│   ├── controlFiles.csv
│   ├── controlTimes.csv
│   ├── mode.csv
│   ├── trivialEmergencyTimes.csv
│   ├── trivialFiles.csv
│   └── trivialTaskTimes.csv
└── styles
    ├── app_styles.css
    └── settings_styles.css
```
You should never modify the "styles" or "scripts" folders. It is also not recommended to directly modify the "storage" folder, since "settings.exe" will modify the files in this folder for you. 

After unzipping the file, the first thing you should do is add the video files you want to play in the app to the folder. As an example, I've added example_control.mp4 and example_trivial.mp4 to the files, which resulted in the following file structure:
```
Autonomous_Driving_with_Tasks_Experiment
├── example_control.mp4
├── example_trivial.mp4
├── run_experiment.exe
├── scripts
│   ├── __pycache__
│   │   ├── change_file_window.cpython-310.pyc
│   │   ├── experiment_window.cpython-310.pyc
│   │   ├── final_window.cpython-310.pyc
│   │   ├── info_window.cpython-310.pyc
│   │   ├── settings_styles.cpython-310.pyc
│   │   └── survey_window.cpython-310.pyc
│   ├── change_file_window.py
│   ├── experiment_window.py
│   ├── final_window.py
│   ├── info_window.py
│   └── survey_window.py
├── settings.exe
├── storage
│   ├── controlFiles.csv
│   ├── controlTimes.csv
│   ├── mode.csv
│   ├── trivialEmergencyTimes.csv
│   ├── trivialFiles.csv
│   └── trivialTaskTimes.csv
└── styles
    ├── app_styles.css
    └── settings_styles.css
```
Next, you should open up "settings.exe". Set the settings for each field, making sure to set the settings for both modes by pressing the "Change Mode" button in the top left corner. Keep in mind that the output file will be created if it doesn't exist in the current directory. All settings will only be locked in after pressing the "Submit" button, so make sure to press that before exiting the window or changing modes. The "Current Mode" as indicated in the top left corner will be the mode used when run_experiment.exe is opened as well. Make sure you finished setting all the settings before opening run_experiment.exe, or the newest changes may not be reflected in the app. Additionally, since all the settings are written to the files in the "storage" folder, please set the settings you want on one computer before distributing the program to all the computers you want to run the experiment on. All your configurations will carry over. 

The two images below show my example settings configuration for each mode:
![trivial_settings.jpg](/doc_imgs/trivial_settings.jpg)
![control_settings.jpg](/doc_imgs/control_settings.jpg)

You can now run the experiment as needed. Since the trivial scenario has everything that the control scenario has as well as a little more, all the images below will be from the trivial scenario. Open up "run_experiment.exe" to start the experiment. You should be greeted with the [Instructions Page](https://github.com/sf200212345/drivingTestProgram#instructions-page):
![instructions_page.jpg](/doc_imgs/instructions_page.jpg)

Pressing the "Ready" button will take you to the [Experiment Page](https://github.com/sf200212345/drivingTestProgram#experiment-page). This page will play the video you previously set in the settings and will prompt the buttons at the timestamps you set. These buttons will only be displayed for as long as you set under "Display Time" in the settings. If the participant doesn't press the button during the display time, a time will still be recorded for them. You can use this to test for systematic error in reaction times (see [Experiment Page](https://github.com/sf200212345/drivingTestProgram#experiment-page)). For the example video I set, the [Experiment Page](https://github.com/sf200212345/drivingTestProgram#experiment-page) looks like this:
![experiment_page_task.jpg](/doc_imgs/experiment_page_task.jpg)
![experiment_page_emergency.jpg](/doc_imgs/experiment_page_emergency.jpg)

After the video ends, the application will immediately bring up the [Survey Page](https://github.com/sf200212345/drivingTestProgram#survey-page). The participant will be prompted to click on the "Open Survey" button and remember their participant ID (numeric only), which should be shown in the browser after they finish their survey. The survey prompt looks like this:
![survey_prompt.jpg](/doc_imgs/survey_prompt.jpg)

Clicking on the button will open the default browser on the computer and take the participant to the link set in the settings. After closing the survey, the participant will be shown the following page:
![survey_input.jpg](/doc_imgs/survey_input.jpg)

After the participant inputs a valid participant ID (see [Survey Page](https://github.com/sf200212345/drivingTestProgram#survey-page)), the [Ending Page](https://github.com/sf200212345/drivingTestProgram#ending-page) will show up:
![ending_page.jpg](/doc_imgs/ending_page.jpg)

Seeing this page means that the data collected during the experiment has successfully been written to the output file defined in the settings. Prior to this page, ***no data would have been written to file***. Participants should not click "X" to exit the application until after they see this page.

After exiting, you can find the data located in the "Autonomous_Driving_with_Tasks_Experiment" folder. I labeled my output file "trivialTasksResults.csv", so my file structure looks like this now:
```
Autonomous_Driving_with_Tasks_Experiment
├── example_control.mp4
├── example_trivial.mp4
├── run_experiment.exe
├── scripts
│   ├── __pycache__
│   │   ├── change_file_window.cpython-310.pyc
│   │   ├── experiment_window.cpython-310.pyc
│   │   ├── final_window.cpython-310.pyc
│   │   ├── info_window.cpython-310.pyc
│   │   ├── settings_styles.cpython-310.pyc
│   │   └── survey_window.cpython-310.pyc
│   ├── change_file_window.py
│   ├── experiment_window.py
│   ├── final_window.py
│   ├── info_window.py
│   └── survey_window.py
├── settings.exe
├── storage
│   ├── controlFiles.csv
│   ├── controlTimes.csv
│   ├── mode.csv
│   ├── trivialEmergencyTimes.csv
│   ├── trivialFiles.csv
│   └── trivialTaskTimes.csv
├── styles
│   ├── app_styles.css
│   └── settings_styles.css
└── trivialTasksResults.csv
```

Opening up "trivialTasksResults.csv" shows me the following:
![results.jpg](/doc_imgs/results.jpg)

The first column will always be the participant ID. The program combines the reaction times for the "I am paying attention" and "Emergency" buttons together, so you will have to sort which reaction times belong to which categories according to the order of the timestamps.

## Notes on run_experiment
May take a little bit to start up

### Instructions Page
All initialization of experiment occurs in this page, so make sure this page is up and running before the participant starts.

### Experiment Page
How to test for systematic error

### Survey Page
Valid participant ID

### Ending Page
Flush all data to files

## Notes on settings
please only .csv or plaintext files for output file
.mov, .mp4 both worked for me for video files

### Storage Files
Which fields correspond to which storage files
