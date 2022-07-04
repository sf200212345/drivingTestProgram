from PyQt6.QtWidgets import QLabel, QGridLayout, QWidget, QPushButton, QLineEdit
import csv

'''
Tells the user what to do in the incoming experiment
Has a settings button that allows the experiment operator to change file names and times
Has an "I'm ready" button to start
'''
class InfoWindow(QWidget):
    def __init__(self, INFO):
        super().__init__()
        
        layout = QGridLayout()

        self.ChangeFileWindow = ChangeFileWindow(INFO)
        layout.addWidget(self.ChangeFileWindow, 0, 1, 4, 2)
        self.ChangeFileWindow.setHidden(True)

        self.changeFileButton = QPushButton("Settings")
        layout.addWidget(self.changeFileButton, 0, 0)

        self.instructions = QLabel("Instructions for control scenario:\nPress the 'Emergency' button when an emergency situation arises.")
        layout.addWidget(self.instructions, 1, 1, 1, 2)
        self.readyButton = QPushButton("Ready")
        layout.addWidget(self.readyButton, 2, 1, 1, 2)
        layout.addWidget(QWidget(), 0, 3)
        layout.addWidget(QWidget(), 3, 0)

        self.setLayout(layout)

        self.changeFileButton.clicked.connect(self.openSettings)
        self.ChangeFileWindow.setSubmitButton(self.closeSettings)

    def setReadyButton(self, parentFunc):
        self.readyButton.clicked.connect(parentFunc)

    def openSettings(self):
        self.ChangeFileWindow.setHidden(False)
        self.instructions.setHidden(True)
        self.readyButton.setHidden(True)
        self.changeFileButton.setHidden(True)
    
    def closeSettings(self):
        self.ChangeFileWindow.setHidden(True)
        self.instructions.setHidden(False)
        self.readyButton.setHidden(False)
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
        videoLayout = QGridLayout()
        videoPrompt0 = QLabel("Current video name for the control (no tasks) scenario:")
        self.videoName = QLabel(self.INFO["videoName"])
        videoPrompt1 = QLabel("Enter new video name (including file extension):")
        self.video = QLineEdit()
        videoLayout.addWidget(videoPrompt0, 0, 0)
        videoLayout.addWidget(self.videoName, 1, 0)
        videoLayout.addWidget(videoPrompt1, 2, 0)
        videoLayout.addWidget(self.video, 3, 0)
        layout.addLayout(videoLayout, 0, 1)

        # module for setting the control output file name
        outputLayout = QGridLayout()
        outputPrompt0 = QLabel("Current output file name for the control (no tasks) scenario:")
        self.outputName = QLabel(self.INFO["outputName"])
        outputPrompt1 = QLabel("Enter new output file name (including file extension):")
        self.output = QLineEdit()
        outputLayout.addWidget(outputPrompt0, 0, 0)
        outputLayout.addWidget(self.outputName, 1, 0)
        outputLayout.addWidget(outputPrompt1, 2, 0)
        outputLayout.addWidget(self.output, 3, 0)
        layout.addLayout(outputLayout, 0, 2)

        # module for setting the control video timestamps
        timestampsLayout = QGridLayout()
        timestampsPrompt0 = QLabel("Current video prompt timestamps for the control (no tasks) scenario:")
        self.timestampsName = QLabel(",".join(self.INFO["timestamps"]))
        timestampsPrompt1 = QLabel("Enter new timestamps as a comma-separated list (no spaces):")
        self.timestamps = QLineEdit()
        timestampsLayout.addWidget(timestampsPrompt0, 0, 0)
        timestampsLayout.addWidget(self.timestampsName, 1, 0)
        timestampsLayout.addWidget(timestampsPrompt1, 2, 0)
        timestampsLayout.addWidget(self.timestamps, 3, 0)
        layout.addLayout(timestampsLayout, 1, 1)

        # module for setting the control button display time
        displayTimeLayout = QGridLayout()
        displayTimePrompt0 = QLabel("Current delay time for button display for the control (no tasks) scenario:")
        self.displayTimeName = QLabel(self.INFO["displayTime"])
        displayTimePrompt1 = QLabel("Enter new delay time (must be greater than the minimal interval in timestamps):")
        self.displayTime = QLineEdit()
        displayTimeLayout.addWidget(displayTimePrompt0, 0, 0)
        displayTimeLayout.addWidget(self.displayTimeName, 1, 0)
        displayTimeLayout.addWidget(displayTimePrompt1, 2, 0)
        displayTimeLayout.addWidget(self.displayTime, 3, 0)
        layout.addLayout(displayTimeLayout, 1, 2)

        submitLayout = QGridLayout()
        submitPrompt = QLabel("Leave the textbox of fields you don't want to change blank.")
        self.submitButton = QPushButton("Submit")
        submitLayout.addWidget(submitPrompt, 0, 0)
        submitLayout.addWidget(self.submitButton, 1, 0)
        layout.addLayout(submitLayout, 3, 1, 1, 2)
        self.setLayout(layout)

        self.submitButton.clicked.connect(self.submitButtonClicked)

    # processes all inputted text and assigns it to the corresponding variables in the INFO dict
    # flushes changed data to internal storage files
    def submitButtonClicked(self):
        if (len(self.video.text()) > 0):
            self.INFO["videoName"] = self.video.text()
            self.video.clear()
            self.videoName.setText(self.INFO["videoName"])

        if (len(self.output.text()) > 0):
            self.INFO["outputName"] = self.output.text()
            self.output.clear()
            self.outputName.setText(self.INFO["outputName"])

        if (len(self.displayTime.text()) > 0):
            self.INFO["displayTime"] = self.displayTime.text()
            self.displayTime.clear()
            self.displayTimeName.setText(self.INFO["displayTime"])

        with open("fileInfo.csv", "w", newline='') as writer:
                csv.writer(writer).writerow([self.INFO["videoName"], self.INFO["outputName"], "controlTimes.csv", self.INFO["displayTime"]])

        if (len(self.timestamps.text()) > 0):
            self.INFO["timestamps"] = self.timestamps.text().split(",")
            self.timestamps.clear()
            self.timestampsName.setText(",".join(self.INFO["timestamps"]))
            with open("controlTimes.csv", "w", newline='') as writer:
                csv.writer(writer).writerow(self.INFO["timestamps"])

    def setSubmitButton(self, parentFunc):
        self.submitButton.clicked.connect(parentFunc)