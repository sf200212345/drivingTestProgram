# drivingTestProgram Documentation
Software developed for a simulated autonomous driving experiment. Built with PyQt6 and packaged with PyInstaller to be distributed to Windows computers. Download the latest app package [here](/Autonomous_Driving_with_Tasks_Experiment.zip).

For developers (really just myself):
You need to have the PyQt6 library downloaded to run this from the command line. You can run "python3 settings_driver.py" to open settings and "python3 app_driver.py" to open the app. PyInstaller commands to package the app are in pyinstall_commands.txt. 

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
- Configure the settings before distributing the .zip package to all computers used for the experiment. The settings will carry over.
- Put the video files in this folder. You can also put the output files in this folder, but the program will create an output file if it doesn't exist in the directory.
- Make sure to configure both modes. Leave the settings app in the mode that you want to run the experiment on when you close it.
- You must press submit for the changes to be written to the storage files. 
- Do not run both settings and run_experiment at the same time. Configure the settings BEFORE opening run_experiment.
- The data from run_experiment will only be written to file AFTER the participant submits a [valid participant ID](https://github.com/sf200212345/drivingTestProgram#survey-page).
- Make sure to test for [systematic error](https://github.com/sf200212345/drivingTestProgram#systematic-error).

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
May take a little bit to start up because all the programming resources it relies on is packaged within the application. Runs most optimally if no other resource-heavy software is running in the background (e.g. any video streaming/calling application, games, etc.). 

### Instructions Page
This is the first page that participants see. It looks like this:
![instructions_page.jpg](/doc_imgs/instructions_page.jpg)

All initialization for the experiment occurs in this page, so make sure this page is up and running before the participant starts. This will ensure that there are no issues prior to the experiment.

### Experiment Page
This is the second page that participants see. This page contains the actual video and reaction time data collection of the experiment. It looks like this:
![experiment_page_task.jpg](/doc_imgs/experiment_page_task.jpg)
![experiment_page_emergency.jpg](/doc_imgs/experiment_page_emergency.jpg)

#### Time collection mechanism and Random Error
The app will check every 100 ms whether a timestamp is near. Specifically, if timestamp - current time is less than 50 ms, the app will display the corresponding button. Once the button is pressed, the app will note down the current time to process later with the given timestamps. Since the time collection mechanism is set up like this, there should be a less-than 50 ms random error on the collected reaction time.

#### Systematic Error
It takes a little bit of time for all of the steps of time collection, so the results from this app won't be perfect. However, there is a observable systematic error that can be tested for. This systematic error will differ based on your computer specs, but it shouldn't differ by a huge range. You should test for systematic error on a computer that would eventually be used in the experiment, replicating the same digital environment as when you actually run the app. 

To test for systematic error, set up all the settings as it would be in the actual experiment, and open "run_experiment" and go to the experiment page. DO NOT press any buttons. This will force the program to collect the latest possible reaction time for each timestamp. The recorded time will be longer than the display time you set in settings, so display time - collected time would be your systematic error. This error should be fairly consistent across all data points. As an example, I set the display time to be 2 seconds, which yielded the following data:
![systematic_error.jpg](/doc_imgs/systematic_error.jpg)

As before, the first column is the participant ID. Please remember that there should be a random error around 50 ms, or 0.05 seconds. The systematic error in this example would be around 0.3 - 0.4 seconds. From testing, it looks like longer display times and longer gaps between timestamps would stablize/lower the systematic error, so it shouldn't be an issue for the actual experiment.

### Survey Page
The survey page consists of the prompt that tells participants to complete the survey and the page to enter their participant ID. These pages look like this:
![survey_prompt.jpg](/doc_imgs/survey_prompt.jpg)
![survey_input.jpg](/doc_imgs/survey_input.jpg)

The program will wait 5 seconds after the "Open Survey" button is pressed before moving onto the next page. This should prevent things like accidentally closing the browser after opening the survey.

The area where the participant is asked to enter their participant ID will check if the entered ID conforms to a certain format when the participant presses the "submit" button. The participant ID must consist only of numbers and contain no whitespace or any special characters. The participant will not be able to move on if the field is left empty. The following error messages will be displayed if the participant ID isn't in the right format:
![survey_empty.jpg](/doc_imgs/survey_empty.jpg)
![survey_invalid.jpg](/doc_imgs/survey_invalid.jpg)

### Ending Page
This is the final page that participants will see. This page looks like this:
![ending_page.jpg](/doc_imgs/ending_page.jpg)

All the data collected in this experiment will be processed and written to the output file defined in settings after the participant presses the "submit" button on the previous page, which prompted participants for their participant ID. As before, after participants see this page, they can safely click "X" to exit out of the application without worrying about the data not being saved.

## Notes on settings
There are two modes available in settings: trivial and control. Trivial refers to the mode where participants have to press a button to stay engaged, while the control doesn't have that feature. Please remember to edit and submit the settings for both modes before distributing the entire folder to other lab computers so you don't need to configure each computer individually. Also make sure that you have submitted the settings you want before opening "run_experiment". 

Please only specify .csv or plaintext files for the output file. Other output file formats may not be supported. Remember that this file will be created by the program if it doesn't exist in the current directory. 

For the video file format, I tested with .mov and .mp4 files. Both of these played without problem. Other common video file formats will probably be okay as well, but I haven't tested them.

### Storage Files
"settings.exe" and "run_experiment.exe" will read all settings from the "storage" folder. Do not change the folder or file names. If you would like to configure these files directly instead of through the settings app, I have listed which fields in the settings app corresponds to which files:

The file structure of the storage folder looks like this:
```
storage
├── controlFiles.csv
├── controlTimes.csv
├── mode.csv
├── trivialEmergencyTimes.csv
├── trivialFiles.csv
└── trivialTaskTimes.csv
```

controlTimes.csv, trivialEmergencyTimes.csv and trivialTaskTimes.csv all store the timestamps entered for each scenario. These are stored on a single line as comma-separated values (there are no whitespaces between any values). If you open the .csv file with Excel, Excel will automatically put commas between separate cells, so just make sure that all the timestamps are on the same row.

mode.csv stores the current mode for "run_experiment". 'T' runs the experiment in Trivial mode, 'C' runs the experiment in Control mode. 

controlFiles.csv and trivialFiles.csv both store 4 values each. The values are in this order: video file, output file, display time of button, survey link. As an example:
![trivialFiles.jpg](/doc_imgs/trivialFiles.jpg)

The video name is example_trivial.mp4, the output file is trivialTasksResults.csv, the display time for buttons is 2 seconds, and the survey link is https://some_survey_link.com.
