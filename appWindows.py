from PyQt6.QtWidgets import QLabel, QGridLayout, QWidget, QPushButton
from PyQt6.QtMultimedia import QMediaPlayer, QAudioOutput
from PyQt6.QtMultimediaWidgets import QVideoWidget
from PyQt6.QtCore import QUrl
import datetime
import csv

OUTPUT = []
STARTTIME = datetime.datetime.now()

# names of files that contains output from either scenario
CONTROLFILENAME = "controlResults.csv"
TRIVIALFILENAME = "trivialTasksResults.csv"

# names of movie files corresponding to each scenario
CONTROLVIDEO = "DrivingControl.mov"
TRIVIALVIDEO = "DrivingTrivialTasks.mov"

# timestamps of tasks/emergencies in either video
CONTROLTIMES = [2.00, 5.37]
TRIVIALTIMES = []

'''
First window you see when starting up the app
Has a title and two buttons
controlButton leads to the video without trivial tasks
trivialButton leads to the video with trivial tasks
'''
class WelcomeWindow(QWidget):
    def __init__(self):
        super().__init__()

        layout = QGridLayout()

        layout.addWidget(QLabel("Welcome! Press one of the buttons below to get started."), 1, 1, 1, 2)
        self.controlButton = QPushButton("Control")
        self.trivialButton = QPushButton("Trivial Tasks")
        layout.addWidget(self.controlButton, 2, 1)
        layout.addWidget(self.trivialButton, 2, 2)
        layout.addWidget(QWidget(), 0, 3)
        layout.addWidget(QWidget(), 3, 0)
        self.setLayout(layout)
    
    def setControlButton(self, parentFunc):
        self.controlButton.clicked.connect(parentFunc)

    def setTrivialButton(self, parentFunc):
        self.trivialButton.clicked.connect(parentFunc)
        
'''
Tells the user what to do in the incoming experiment
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
Upon button press record the time, store time in OUTPUT global variable
'''
class ExperimentWindow(QWidget):
    def __init__(self):
        super().__init__()

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
            self.player.setSource(QUrl.fromLocalFile(CONTROLVIDEO))
        else:
            self.longEmergencyButton.setHidden(True)
            self.player.setSource(QUrl.fromLocalFile(TRIVIALVIDEO))

    def startVideo(self):
        self.player.play()
        STARTTIME = datetime.datetime.now()

    def stopVideo(self):
        self.player.stop()

    def setCompleteButton(self, parentFunc):
        self.completeButton.clicked.connect(parentFunc)

    def taskButtonClicked(self):
        OUTPUT.append(datetime.datetime.now())
    
    def emergencyButtonClicked(self):
        OUTPUT.append(datetime.datetime.now())
    
    def longEmergencyButtonClicked(self):
        OUTPUT.append(datetime.datetime.now())

'''
Displays a "finished" screen
Processes data collected from ExperimentWindow
Flushes results to csv file
'''
class FinalWindow(QWidget):
    def __init__(self):
        super().__init__()

        layout = QGridLayout()

        layout.addWidget(QLabel("Finished! Close the window."), 1, 1, 2, 2)
        layout.addWidget(QWidget(), 0, 3)
        layout.addWidget(QWidget(), 3, 0)
        self.setLayout(layout)
    # pass output and starttime as variables in here
    def flushToCSV(self, scenario):
        if scenario:
            if len(OUTPUT) != len(CONTROLTIMES):
                OUTPUT = ["I", "Invalid Data: Number of button-presses must equal the number of prompts (tasks/emergencies) in video."]
            else:
                for i in range(len(OUTPUT)):
                    OUTPUT[i] = (OUTPUT[i] - STARTTIME).total_seconds() - CONTROLTIMES[i]
            with open(CONTROLFILENAME, "a", newline='') as writer:
                csv.writer(writer).writerow(OUTPUT)
        else:
            if len(OUTPUT) != len(TRIVIALTIMES):
                OUTPUT = ["I", "Invalid Data: Number of button-presses must equal the number of prompts (tasks/emergencies) in video."]
            else:
                for i in range(len(OUTPUT)):
                    OUTPUT[i] = (OUTPUT[i] - STARTTIME).total_seconds() - TRIVIALTIMES[i]
            with open(TRIVIALFILENAME, "a", newline='') as writer:
                csv.writer(writer).writerow(OUTPUT)
