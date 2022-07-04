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
    def __init__(self, INFO):
        super().__init__()
        
        self.INFO = INFO
        self.timestamps = []
        self.timestampsLength = 0
        self.clicked = True
        self.currTimestamp = 0

        layout = QGridLayout()

        self.longEmergencyButton = QPushButton("Emergency")
        self.completeButton = QPushButton("Complete")
        
        self.player = QMediaPlayer()
        self.video = QVideoWidget()
        self.player.setVideoOutput(self.video)
        self.audio = QAudioOutput()
        self.player.setAudioOutput(self.audio)
        self.video.show()
        
        layout.addWidget(self.video, 0, 0, 3, 4)
        layout.addWidget(self.longEmergencyButton, 3, 1, 1, 1)
        layout.addWidget(self.completeButton, 1, 1, 2, 2)
        layout.addWidget(QPushButton(), 3, 3)
        layout.addWidget(QPushButton(), 3, 0)
        self.setLayout(layout)

        self.longEmergencyButton.clicked.connect(self.longEmergencyButtonClicked)
        self.player.positionChanged.connect(self.positionChanged)
        self.player.playbackStateChanged.connect(self.playbackStateChanged)

    # render video and start on ready button click
    def renderVideo(self):
        self.player.setSource(QUrl.fromLocalFile(self.INFO["videoName"]))

        self.video.setHidden(False)
        self.completeButton.setHidden(True)
        self.longEmergencyButton.setHidden(True)

        self.clicked = True
        self.currTimestamp = 0
        self.timestamps.clear()
        self.timestampsLength = len(self.INFO["timestamps"])

        for i in range(self.timestampsLength):
            self.timestamps.append(int(float(self.INFO["timestamps"][i]) * 1000))
            self.timestamps.append(int((float(self.INFO["timestamps"][i]) + float(self.INFO["displayTime"])) * 1000))
        self.timestampsLength = len(self.timestamps)
        
        self.player.play()
        self.INFO["startTime"] = datetime.datetime.now()
        
    def setCompleteButton(self, parentFunc):
        self.completeButton.clicked.connect(parentFunc)
    
    def longEmergencyButtonClicked(self):
        self.INFO["output"].append(datetime.datetime.now())
        self.longEmergencyButton.setHidden(True)
        self.currTimestamp += 1
        self.clicked = True

    def positionChanged(self, position):   
        if (self.currTimestamp < self.timestampsLength and (self.timestamps[self.currTimestamp] - position) < 100):
            if (self.clicked):
                self.clicked = False
                self.longEmergencyButton.setHidden(False)
            # if emergency button wasn't clicked in the interval
            else:
                self.clicked = True
                self.longEmergencyButton.setHidden(True)
                self.INFO["output"].append(datetime.datetime.now())
            self.currTimestamp += 1

    def playbackStateChanged(self, state):
        if (state == QMediaPlayer.PlaybackState.StoppedState):
            self.video.setHidden(True)
            self.longEmergencyButton.setHidden(True)
            self.completeButton.setHidden(False)
