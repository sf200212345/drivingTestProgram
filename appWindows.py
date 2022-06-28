from PyQt6.QtWidgets import QLabel, QGridLayout, QWidget, QPushButton, QLineEdit
from PyQt6.QtMultimedia import QMediaPlayer, QAudioOutput
from PyQt6.QtMultimediaWidgets import QVideoWidget
from PyQt6.QtCore import QUrl
import datetime
import csv
'''
# Global variables that contain all necessary info for the application to run
INFO = {
    # contains all the timestamps when the user pressed the button
    "output": [],

    # start time of computer OS when the video starts playing
    "startTime": datetime.datetime.now(),

    # file names of where to write the results
    "controlFileName": "",
    "trivialFileName": "",
    
    # file names of videos to be played
    "controlVideo": "",
    "trivialVideo": "",

    # timestamps of prompts in the videos
    "controlTimes": [],
    "trivialTimes": []
}
'''
'''
First window you see when starting up the app
controlButton leads to the video without trivial tasks
trivialButton leads to the video with trivial tasks
Settings allows you to set file names of input/output and timestamps on the video
'''
class WelcomeWindow(QWidget):
    def __init__(self, INFO):
        super().__init__()

        # self.initializeGlobalVariables()
        layout = QGridLayout()
        self.INFO = INFO
        self.title = QLabel("Welcome! Press one of the buttons below to get started.")
        layout.addWidget(self.title, 1, 1, 1, 2)

        self.ChangeFileWindow = ChangeFileWindow(self.INFO)
        layout.addWidget(self.ChangeFileWindow, 0, 1, 4, 2)
        self.ChangeFileWindow.setHidden(True)

        self.controlButton = QPushButton("Control")
        self.trivialButton = QPushButton("Trivial Tasks")
        self.changeFileButton = QPushButton("Settings")
        layout.addWidget(self.changeFileButton, 0, 0)
        layout.addWidget(self.controlButton, 2, 1)
        layout.addWidget(self.trivialButton, 2, 2)

        layout.addWidget(QWidget(), 0, 3)
        layout.addWidget(QWidget(), 3, 0)
        self.setLayout(layout)

        self.changeFileButton.clicked.connect(self.openSettings)
        self.ChangeFileWindow.setSubmitButton(self.closeSettings)
    
    def setControlButton(self, parentFunc):
        self.controlButton.clicked.connect(parentFunc)

    def setTrivialButton(self, parentFunc):
        self.trivialButton.clicked.connect(parentFunc)

    '''
    # initializes global variables from the file names stored in storage file "fileNames.csv"
    def initializeGlobalVariables(self):
        with open("fileNames.csv", newline='') as fileName:
            reader = csv.reader(fileName)
            for row in reader:
                INFO["controlVideo"] = row[0]
                INFO["trivialVideo"] = row[1]
                INFO["controlFileName"] = row[2]
                INFO["trivialFileName"] = row[3]
                with open(row[4], newline='') as controlTimes:
                    controlReader = csv.reader(controlTimes)
                    for i in controlReader:
                        INFO["controlTimes"] = i
                with open(row[5], newline='') as trivialTimes:
                    trivialReader = csv.reader(trivialTimes)
                    for j in trivialReader:
                        INFO["trivialTimes"] = j

    '''
    
    def openSettings(self):
        self.ChangeFileWindow.setHidden(False)
        self.title.setHidden(True)
        self.controlButton.setHidden(True)
        self.trivialButton.setHidden(True)
        self.changeFileButton.setHidden(True)
    
    def closeSettings(self):
        self.ChangeFileWindow.setHidden(True)
        self.title.setHidden(False)
        self.controlButton.setHidden(False)
        self.trivialButton.setHidden(False)
        self.changeFileButton.setHidden(False)

        
'''
The user (supervisor of experiment) can change the file name of the videos and output here
They can also change the timestamps on the videos where prompts show up
On submit, all inputted text will be flushed to the corresponding internal storage files
'''
class ChangeFileWindow(QWidget):
    def __init__(self, INFO):
        super().__init__()

        layout = QGridLayout()
        self.INFO = INFO
        # module for setting the control video name
        controlVideoLayout = QGridLayout()
        controlVideoPrompt0 = QLabel("Current video name for the no-task scenario:")
        self.controlVideoName = QLabel(self.INFO["controlVideo"])
        controlVideoPrompt1 = QLabel("Enter new video name (including file extension):")
        self.controlVideo = QLineEdit()
        controlVideoLayout.addWidget(controlVideoPrompt0, 0, 0)
        controlVideoLayout.addWidget(self.controlVideoName, 1, 0)
        controlVideoLayout.addWidget(controlVideoPrompt1, 2, 0)
        controlVideoLayout.addWidget(self.controlVideo, 3, 0)
        layout.addLayout(controlVideoLayout, 0, 1)

        # module for setting the trivial video name
        trivialVideoLayout = QGridLayout()
        trivialVideoPrompt0 = QLabel("Current video name for the trivial-task scenario:")
        self.trivialVideoName = QLabel(self.INFO["trivialVideo"])
        trivialVideoPrompt1 = QLabel("Enter new video name (including file extension):")
        self.trivialVideo = QLineEdit()
        trivialVideoLayout.addWidget(trivialVideoPrompt0, 0, 0)
        trivialVideoLayout.addWidget(self.trivialVideoName, 1, 0)
        trivialVideoLayout.addWidget(trivialVideoPrompt1, 2, 0)
        trivialVideoLayout.addWidget(self.trivialVideo, 3, 0)
        layout.addLayout(trivialVideoLayout, 0, 2)

        # module for setting the control output file name
        controlResultLayout = QGridLayout()
        controlResultPrompt0 = QLabel("Current output file name for the no-task scenario:")
        self.controlResultName = QLabel(self.INFO["controlFileName"])
        controlResultPrompt1 = QLabel("Enter new output file name (including file extension):")
        self.controlResult = QLineEdit()
        controlResultLayout.addWidget(controlResultPrompt0, 0, 0)
        controlResultLayout.addWidget(self.controlResultName, 1, 0)
        controlResultLayout.addWidget(controlResultPrompt1, 2, 0)
        controlResultLayout.addWidget(self.controlResult, 3, 0)
        layout.addLayout(controlResultLayout, 1, 1)

        # module for setting the trivial output file name
        trivialResultLayout = QGridLayout()
        trivialResultPrompt0 = QLabel("Current output file name for the trivial-task scenario:")
        self.trivialResultName = QLabel(self.INFO["trivialFileName"])
        trivialResultPrompt1 = QLabel("Enter new output file name (including file extension):")
        self.trivialResult = QLineEdit()
        trivialResultLayout.addWidget(trivialResultPrompt0, 0, 0)
        trivialResultLayout.addWidget(self.trivialResultName, 1, 0)
        trivialResultLayout.addWidget(trivialResultPrompt1, 2, 0)
        trivialResultLayout.addWidget(self.trivialResult, 3, 0)
        layout.addLayout(trivialResultLayout, 1, 2)

        # module for setting the control video timestamps
        controlTimesLayout = QGridLayout()
        controlTimesPrompt0 = QLabel("Current video prompt timestamps for the no-task scenario:")
        self.controlTimesName = QLabel(",".join(self.INFO["controlTimes"]))
        controlTimesPrompt1 = QLabel("Enter new timestamps as a comma-separated list (no spaces):")
        self.controlTimes = QLineEdit()
        controlTimesLayout.addWidget(controlTimesPrompt0, 0, 0)
        controlTimesLayout.addWidget(self.controlTimesName, 1, 0)
        controlTimesLayout.addWidget(controlTimesPrompt1, 2, 0)
        controlTimesLayout.addWidget(self.controlTimes, 3, 0)
        layout.addLayout(controlTimesLayout, 2, 1)

        # module for setting the trivial video timestamps
        trivialTimesLayout = QGridLayout()
        trivialTimesPrompt0 = QLabel("Current video prompt timestamps for the trivial-task scenario:")
        self.trivialTimesName = QLabel(",".join(self.INFO["trivialTimes"]))
        trivialTimesPrompt1 = QLabel("Enter new timestamps as a comma-separated list (no spaces):")
        self.trivialTimes = QLineEdit()
        trivialTimesLayout.addWidget(trivialTimesPrompt0, 0, 0)
        trivialTimesLayout.addWidget(self.trivialTimesName, 1, 0)
        trivialTimesLayout.addWidget(trivialTimesPrompt1, 2, 0)
        trivialTimesLayout.addWidget(self.trivialTimes, 3, 0)
        layout.addLayout(trivialTimesLayout, 2, 2)

        submitLayout = QGridLayout()
        submitPrompt = QLabel("Leave the textbox of fields you don't want to change blank.")
        self.submitButton = QPushButton("Submit")
        submitLayout.addWidget(submitPrompt, 0, 0)
        submitLayout.addWidget(self.submitButton, 1, 0)
        layout.addLayout(submitLayout, 3, 1, 1, 2)
        self.setLayout(layout)

        self.submitButton.clicked.connect(self.submitButtonClicked)

    # processes all inputted text and assigns it to the corresponding global variables
    # flushes changed data to internal storage files
    def submitButtonClicked(self):
        if (len(self.controlVideo.text()) > 0):
            self.INFO["controlVideo"] = self.controlVideo.text()
            self.controlVideo.clear()
            self.controlVideoName.setText(self.INFO["controlVideo"])

        if (len(self.trivialVideo.text()) > 0):
            self.INFO["trivialVideo"] = self.trivialVideo.text()
            self.trivialVideo.clear()
            self.trivialVideoName.setText(self.INFO["trivialVideo"])

        if (len(self.controlResult.text()) > 0):
            self.INFO["controlFileName"] = self.controlResult.text()
            self.controlResult.clear()
            self.controlResultName.setText(self.INFO["controlFileName"])

        if (len(self.trivialResult.text()) > 0):
            self.INFO["trivialFileName"] = self.trivialResult.text()
            self.trivialResult.clear()
            self.trivialResultName.setText(self.INFO["trivialFileName"])
        
        with open("fileNames.csv", "w", newline='') as writer:
                csv.writer(writer).writerow([self.INFO["controlVideo"], self.INFO["trivialVideo"], self.INFO["controlFileName"], self.INFO["trivialFileName"], "controlTimes.csv", "trivialTimes.csv"])

        if (len(self.controlTimes.text()) > 0):
            self.INFO["controlTimes"] = self.controlTimes.text().split(",")
            self.controlTimes.clear()
            self.controlTimesName.setText(",".join(self.INFO["controlTimes"]))
            with open("controlTimes.csv", "w", newline='') as writer:
                csv.writer(writer).writerow(self.INFO["controlTimes"])
        
        if (len(self.trivialTimes.text()) > 0):
            self.INFO["trivialTimes"] = self.trivialTimes.text().split(",")
            self.trivialTimes.clear()
            self.trivialTimesName.setText(",".join(self.INFO["trivialTimes"]))
            with open("trivialTimes.csv", "w", newline='') as writer:
                csv.writer(writer).writerow(self.INFO["trivialTimes"])

    def setSubmitButton(self, parentFunc):
        self.submitButton.clicked.connect(parentFunc)

'''
Tells the user what to do in the incoming experiment based on the previous scenario chosen
Has an "I'm ready" button to start
'''
class InfoWindow(QWidget):
    def __init__(self):
        super().__init__()

        layout = QGridLayout()

        self.instructions = QLabel()
        layout.addWidget(self.instructions, 1, 1, 1, 2)
        self.readyButton = QPushButton("Ready")
        layout.addWidget(self.readyButton, 2, 1, 1, 2)
        layout.addWidget(QWidget(), 0, 3)
        layout.addWidget(QWidget(), 3, 0)
        self.setLayout(layout)
    
    def renderOnScenario(self, scenario):
        if scenario:
            self.instructions.setText("Instructions for control scenario:\nPress the 'Emergency' button when an emergency situation arises.")
        else:
            self.instructions.setText("Instructions for trivial scenario:\nPress the 'Do Task' button when prompted and the 'Emergency' button when an emergency situation arises.")

    def setReadyButton(self, parentFunc):
        self.readyButton.clicked.connect(parentFunc)

'''
Displays the video and two/one buttons to press depending on the selected scenario
When video starts, store the OS time as INFO["startTime] for later processing
Upon button press record the time, store time in INFO["output"] global variable
'''
class ExperimentWindow(QWidget):
    def __init__(self, INFO):
        super().__init__()

        self.INFO = INFO
        layout = QGridLayout()
        self.taskButton = QPushButton("Do Task")
        self.emergencyButton = QPushButton("Emergency")
        self.longEmergencyButton = QPushButton("Emergency")
        self.completeButton = QPushButton("Complete")
        
        self.player = QMediaPlayer()
        self.video = QVideoWidget()
        self.player.setVideoOutput(self.video)
        self.audio = QAudioOutput()
        self.player.setAudioOutput(self.audio)
        self.video.show()

        layout.addWidget(self.video, 0, 0, 2, 4)
        layout.addWidget(self.taskButton, 2, 1)
        layout.addWidget(self.emergencyButton, 2, 2)
        layout.addWidget(self.longEmergencyButton, 2, 1, 1, 2)
        layout.addWidget(self.completeButton, 3, 1, 1, 2)
        layout.addWidget(QWidget(), 0, 3)
        layout.addWidget(QWidget(), 3, 0)
        self.setLayout(layout)

        self.taskButton.clicked.connect(self.taskButtonClicked)
        self.emergencyButton.clicked.connect(self.emergencyButtonClicked)
        self.longEmergencyButton.clicked.connect(self.longEmergencyButtonClicked)

    def renderOnScenario(self, scenario):
        if scenario:
            self.taskButton.setHidden(True)
            self.emergencyButton.setHidden(True)
            self.player.setSource(QUrl.fromLocalFile(self.INFO["controlVideo"]))
        else:
            self.longEmergencyButton.setHidden(True)
            self.player.setSource(QUrl.fromLocalFile(self.INFO["trivialVideo"]))

    def startVideo(self):
        self.player.play()
        self.INFO["startTime"] = datetime.datetime.now()

    def stopVideo(self):
        self.player.stop()

    def setCompleteButton(self, parentFunc):
        self.completeButton.clicked.connect(parentFunc)

    def taskButtonClicked(self):
        self.INFO["output"].append(datetime.datetime.now())
    
    def emergencyButtonClicked(self):
        self.INFO["output"].append(datetime.datetime.now())
    
    def longEmergencyButtonClicked(self):
        self.INFO["output"].append(datetime.datetime.now())

'''
Displays a "finished" screen
Processes data collected from ExperimentWindow
Flushes results to csv file
'''
class FinalWindow(QWidget):
    def __init__(self, INFO):
        super().__init__()

        self.INFO = INFO
        layout = QGridLayout()

        layout.addWidget(QLabel("Finished! Close the window."), 1, 1, 2, 2)
        layout.addWidget(QWidget(), 0, 3)
        layout.addWidget(QWidget(), 3, 0)
        self.setLayout(layout)
        
    def flushToCSV(self, scenario):
        print(self.INFO["controlTimes"])
        if scenario:
            if len(self.INFO["output"]) != len(self.INFO["controlTimes"]):
                self.INFO["output"] = ["I", "Invalid Data: Number of button-presses must equal the number of prompts (tasks/emergencies) in video."]
            else:
                for i in range(len(self.INFO["output"])):
                    self.INFO["output"][i] = (self.INFO["output"][i] - self.INFO["startTime"]).total_seconds() - float(self.INFO["controlTimes"][i])
            with open(self.INFO["controlFileName"], "a", newline='') as writer:
                csv.writer(writer).writerow(self.INFO["output"])
        else:
            if len(self.INFO["output"]) != len(self.INFO["trivialTimes"]):
                self.INFO["output"] = ["I", "Invalid Data: Number of button-presses must equal the number of prompts (tasks/emergencies) in video."]
            else:
                for i in range(len(self.INFO["output"])):
                    self.INFO["output"][i] = (self.INFO["output"][i] - self.INFO["startTime"]).total_seconds() - float(self.INFO["trivialTimes"][i])
            with open(self.INFO["trivialFileName"], "a", newline='') as writer:
                csv.writer(writer).writerow(self.INFO["output"])
