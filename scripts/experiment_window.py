from PyQt6.QtWidgets import QGridLayout, QWidget, QPushButton
from PyQt6.QtMultimedia import QMediaPlayer, QAudioOutput
from PyQt6.QtMultimediaWidgets import QVideoWidget
from PyQt6.QtCore import QUrl
import datetime

'''
Displays the video and two/one buttons to press depending on the selected scenario
When video starts, store the OS time as INFO["startTime] for later processing
Upon button press record the time, store time in INFO["output"]
'''
class ExperimentWindow(QWidget):
    def __init__(self, INFO, scenario, videoFinished):
        super().__init__()

        self.INFO = INFO
        self.videoFinished = videoFinished
        if scenario == "C":
            self.timestamps = []
            for i in range(len(self.INFO["timestamps"])):
                self.timestamps.append(int(float(self.INFO["timestamps"][i]) * 1000))
                self.timestamps.append(int((float(self.INFO["timestamps"][i]) + float(self.INFO["displayTime"])) * 1000))
            self.timestampsLength = len(self.timestamps)
            self.currTimestamp = 0
            self.clicked = True
        else:
            self.emergencyTimes = []
            for i in range(len(self.INFO["timestamps"])):
                self.emergencyTimes.append(int(float(self.INFO["timestamps"][i]) * 1000))
                self.emergencyTimes.append(int((float(self.INFO["timestamps"][i]) + float(self.INFO["displayTime"])) * 1000))
            self.emergencyLength = len(self.emergencyTimes)
            self.currEmergency = 0
            self.emergencyClicked = True

            self.taskTimes = []
            for i in range(len(self.INFO["taskTimes"])):
                self.taskTimes.append(int(float(self.INFO["taskTimes"][i]) * 1000))
                self.taskTimes.append(int((float(self.INFO["taskTimes"][i]) + float(self.INFO["displayTime"])) * 1000))
            self.taskLength = len(self.taskTimes)
            self.currTask = 0
            self.taskClicked = True
            
        self.output = []

        layout = QGridLayout()

        self.emergencyButton = QPushButton("Emergency")
        if scenario == "T":
            self.taskButton = QPushButton("I am paying attention")
            self.taskButton.setObjectName("taskButton")
            layout.addWidget(self.taskButton, 3, 2, 1, 1)
            self.taskButton.setHidden(True)
        
        self.player = QMediaPlayer()
        self.video = QVideoWidget()
        self.player.setVideoOutput(self.video)
        self.audio = QAudioOutput()
        self.player.setAudioOutput(self.audio)
        self.video.show()
        self.player.setSource(QUrl.fromLocalFile(self.INFO["videoName"]))

        self.emergencyButton.setObjectName("emergencyButton")
        self.video.setObjectName("video")

        layout.addWidget(self.video, 0, 0, 3, 4)
        layout.addWidget(self.emergencyButton, 3, 1, 1, 1)
        self.emergencyButton.setHidden(True)
        
        self.buttonSpacer1 = QPushButton()
        self.buttonSpacer2 = QPushButton()
        self.buttonSpacer1.setObjectName("spacer")
        self.buttonSpacer2.setObjectName("spacer")
        layout.addWidget(self.buttonSpacer1, 3, 3)
        layout.addWidget(self.buttonSpacer2, 3, 0)
        self.setLayout(layout)

        if scenario == "C":
            self.emergencyButton.clicked.connect(self.emergencyButtonClickedControl)
            self.player.positionChanged.connect(self.positionChangedControl)
        else:
            self.emergencyButton.clicked.connect(self.emergencyButtonClickedTrivial)
            self.taskButton.clicked.connect(self.taskButtonClickedTrivial)
            self.player.positionChanged.connect(self.positionChangedTrivialEmergency)
            self.player.positionChanged.connect(self.positionChangedTrivialTask)
        self.player.playbackStateChanged.connect(self.playbackStateChanged)
        
    # render video and start on ready button click
    def renderVideo(self):
        self.player.play()
        self.INFO["startTime"] = datetime.datetime.now()
    
    def emergencyButtonClickedControl(self):
        self.output.append(datetime.datetime.now())
        self.emergencyButton.setHidden(True)
        self.currTimestamp += 1
        self.clicked = True
    
    def emergencyButtonClickedTrivial(self):
        self.output.append(datetime.datetime.now())
        self.emergencyButton.setHidden(True)
        self.currEmergency += 1
        self.emergencyClicked = True
    
    def taskButtonClickedTrivial(self):
        self.output.append(datetime.datetime.now())
        self.taskButton.setHidden(True)
        self.currTask += 1
        self.taskClicked = True

    def positionChangedControl(self, position):   
        if (self.currTimestamp < self.timestampsLength and (self.timestamps[self.currTimestamp] - position) < 100):
            if (self.clicked):
                self.clicked = False
                self.emergencyButton.setHidden(False)
            # if emergency button wasn't clicked in the interval
            else:
                self.clicked = True
                self.emergencyButton.setHidden(True)
                self.output.append(datetime.datetime.now())
            self.currTimestamp += 1

    def positionChangedTrivialEmergency(self, position):   
        if (self.currEmergency < self.emergencyLength and (self.emergencyTimes[self.currEmergency] - position) < 100):
            if (self.emergencyClicked):
                self.emergencyClicked = False
                self.emergencyButton.setHidden(False)
            # if emergency button wasn't clicked in the interval
            else:
                self.emergencyClicked = True
                self.emergencyButton.setHidden(True)
                self.output.append(datetime.datetime.now())
            self.currEmergency += 1

    def positionChangedTrivialTask(self, position):   
        if (self.currTask < self.taskLength and (self.taskTimes[self.currTask] - position) < 100):
            if (self.taskClicked):
                self.taskClicked = False
                self.taskButton.setHidden(False)
            # if emergency button wasn't clicked in the interval
            else:
                self.taskClicked = True
                self.taskButton.setHidden(True)
                self.output.append(datetime.datetime.now())
            self.currTask += 1

    def playbackStateChanged(self, state):
        if (state == QMediaPlayer.PlaybackState.StoppedState):
            self.INFO["output"] = self.output
            self.videoFinished()