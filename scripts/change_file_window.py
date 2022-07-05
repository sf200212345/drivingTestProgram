from PyQt6.QtWidgets import QWidget, QGridLayout, QLabel, QLineEdit, QPushButton
import csv

class ChangeFileWindowControl(QWidget):
    def __init__(self, CINFO):
        super().__init__()

        self.INFO = CINFO
        layout = QGridLayout()

        self.changeWindowButton = QPushButton("Current Mode: Control\nPress to switch")
        layout.addWidget(self.changeWindowButton, 0, 0)

        # module for setting the control video name
        videoLayout = QGridLayout()
        videoPrompt0 = QLabel("Current video name for the control (no tasks) scenario:")
        self.videoName = QLabel(self.INFO["videoName"])
        self.videoPrompt1 = QLabel("Enter new video name (including file extension):")
        self.video = QLineEdit()
        self.videoPrompt1.setHidden(True)
        self.video.setHidden(True)
        videoLayout.addWidget(videoPrompt0, 0, 0)
        videoLayout.addWidget(self.videoName, 1, 0)
        videoLayout.addWidget(self.videoPrompt1, 2, 0)
        videoLayout.addWidget(self.video, 3, 0)
        layout.addLayout(videoLayout, 1, 1)

        # module for setting the control output file name
        outputLayout = QGridLayout()
        outputPrompt0 = QLabel("Current output file name for the control (no tasks) scenario:")
        self.outputName = QLabel(self.INFO["outputName"])
        self.outputPrompt1 = QLabel("Enter new output file name (including file extension):")
        self.output = QLineEdit()
        self.outputPrompt1.setHidden(True)
        self.output.setHidden(True)
        outputLayout.addWidget(outputPrompt0, 0, 0)
        outputLayout.addWidget(self.outputName, 1, 0)
        outputLayout.addWidget(self.outputPrompt1, 2, 0)
        outputLayout.addWidget(self.output, 3, 0)
        layout.addLayout(outputLayout, 1, 2)

        # module for setting the control video timestamps
        timestampsLayout = QGridLayout()
        timestampsPrompt0 = QLabel("Current video prompt timestamps (emergencies) for the control (no tasks) scenario:")
        self.timestampsName = QLabel(",".join(self.INFO["timestamps"]))
        self.timestampsPrompt1 = QLabel("Enter new timestamps as a comma-separated list (no spaces):")
        self.timestamps = QLineEdit()
        self.timestampsPrompt1.setHidden(True)
        self.timestamps.setHidden(True)
        timestampsLayout.addWidget(timestampsPrompt0, 0, 0)
        timestampsLayout.addWidget(self.timestampsName, 1, 0)
        timestampsLayout.addWidget(self.timestampsPrompt1, 2, 0)
        timestampsLayout.addWidget(self.timestamps, 3, 0)
        layout.addLayout(timestampsLayout, 2, 1)

        # module for setting the control button display time
        displayTimeLayout = QGridLayout()
        displayTimePrompt0 = QLabel("Current delay time for button display for the control (no tasks) scenario:")
        self.displayTimeName = QLabel(self.INFO["displayTime"])
        self.displayTimePrompt1 = QLabel("Enter new delay time (must be greater than the minimal interval in timestamps):")
        self.displayTime = QLineEdit()
        self.displayTimePrompt1.setHidden(True)
        self.displayTime.setHidden(True)
        displayTimeLayout.addWidget(displayTimePrompt0, 0, 0)
        displayTimeLayout.addWidget(self.displayTimeName, 1, 0)
        displayTimeLayout.addWidget(self.displayTimePrompt1, 2, 0)
        displayTimeLayout.addWidget(self.displayTime, 3, 0)
        layout.addLayout(displayTimeLayout, 2, 2)

        submitLayout = QGridLayout()
        self.editPrompt = QLabel("Press the Edit button to change settings.")
        self.editButton = QPushButton("Edit")
        self.submitPrompt = QLabel("Leave the textbox of fields you don't want to change blank. Press the Submit button to preserve changes.")
        self.submitButton = QPushButton("Submit")
        submitLayout.addWidget(self.editPrompt, 0, 0)
        submitLayout.addWidget(self.editButton, 1, 0)
        submitLayout.addWidget(self.submitPrompt, 0, 0)
        submitLayout.addWidget(self.submitButton, 1, 0)
        self.submitButton.setHidden(True)
        self.submitPrompt.setHidden(True)
        layout.addLayout(submitLayout, 3, 1, 1, 2)

        self.editButton.clicked.connect(self.editButtonClicked)
        self.submitButton.clicked.connect(self.submitButtonClicked)
        self.submitButton.clicked.connect(self.flushToFiles)
        
        self.setLayout(layout)
    
    def setChangeWindowButton(self, parentFunc):
        self.changeWindowButton.clicked.connect(parentFunc)

    def editButtonClicked(self):
        self.editButton.setHidden(True)
        self.editPrompt.setHidden(True)
        self.submitButton.setHidden(False)
        self.submitPrompt.setHidden(False)
        self.videoPrompt1.setHidden(False)
        self.video.setHidden(False)
        self.outputPrompt1.setHidden(False)
        self.output.setHidden(False)
        self.timestampsPrompt1.setHidden(False)
        self.timestamps.setHidden(False)
        self.displayTimePrompt1.setHidden(False)
        self.displayTime.setHidden(False)

    def submitButtonClicked(self):
        self.editButton.setHidden(False)
        self.editPrompt.setHidden(False)
        self.submitButton.setHidden(True)
        self.submitPrompt.setHidden(True)
        self.videoPrompt1.setHidden(True)
        self.video.setHidden(True)
        self.outputPrompt1.setHidden(True)
        self.output.setHidden(True)
        self.timestampsPrompt1.setHidden(True)
        self.timestamps.setHidden(True)
        self.displayTimePrompt1.setHidden(True)
        self.displayTime.setHidden(True)

    def flushToFiles(self):
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

        with open("./storage/controlFiles.csv", "w", newline='') as writer:
                csv.writer(writer).writerow([self.INFO["videoName"], self.INFO["outputName"], self.INFO["displayTime"]])

        if (len(self.timestamps.text()) > 0):
            self.INFO["timestamps"] = self.timestamps.text().split(",")
            self.timestamps.clear()
            self.timestampsName.setText(",".join(self.INFO["timestamps"]))
            with open("./storage/controlTimes.csv", "w", newline='') as writer:
                csv.writer(writer).writerow(self.INFO["timestamps"])

class ChangeFileWindowTrivial(QWidget):
    def __init__(self, TINFO):
        super().__init__()

        self.INFO = TINFO
        layout = QGridLayout()

        self.changeWindowButton = QPushButton("Current Mode: Trivial\nPress to switch")
        layout.addWidget(self.changeWindowButton, 0, 0)

        # module for setting the trivial video name
        videoLayout = QGridLayout()
        videoPrompt0 = QLabel("Current video name for the trivial (with tasks) scenario:")
        self.videoName = QLabel(self.INFO["videoName"])
        self.videoPrompt1 = QLabel("Enter new video name (including file extension):")
        self.video = QLineEdit()
        self.videoPrompt1.setHidden(True)
        self.video.setHidden(True)
        videoLayout.addWidget(videoPrompt0, 0, 0)
        videoLayout.addWidget(self.videoName, 1, 0)
        videoLayout.addWidget(self.videoPrompt1, 2, 0)
        videoLayout.addWidget(self.video, 3, 0)
        layout.addLayout(videoLayout, 1, 1)

        # module for setting the trival output file name
        outputLayout = QGridLayout()
        outputPrompt0 = QLabel("Current output file name for the trivial (with tasks) scenario:")
        self.outputName = QLabel(self.INFO["outputName"])
        self.outputPrompt1 = QLabel("Enter new output file name (including file extension):")
        self.output = QLineEdit()
        self.outputPrompt1.setHidden(True)
        self.output.setHidden(True)
        outputLayout.addWidget(outputPrompt0, 0, 0)
        outputLayout.addWidget(self.outputName, 1, 0)
        outputLayout.addWidget(self.outputPrompt1, 2, 0)
        outputLayout.addWidget(self.output, 3, 0)
        layout.addLayout(outputLayout, 1, 2)

        # module for setting the trivial video timestamps
        timestampsLayout = QGridLayout()
        taskTimestampsPrompt0 = QLabel("Current video prompt timestamps (tasks) for the trivial (with tasks) scenario:")
        self.taskTimestampsName = QLabel(",".join(self.INFO["taskTimestamps"]))
        self.taskTimestampsPrompt1 = QLabel("Enter new timestamps as a comma-separated list (no spaces):")
        self.taskTimestamps = QLineEdit()
        self.taskTimestampsPrompt1.setHidden(True)
        self.taskTimestamps.setHidden(True)
        timestampsLayout.addWidget(taskTimestampsPrompt0, 0, 0)
        timestampsLayout.addWidget(self.taskTimestampsName, 1, 0)
        timestampsLayout.addWidget(self.taskTimestampsPrompt1, 2, 0)
        timestampsLayout.addWidget(self.taskTimestamps, 3, 0)
        emergencyTimestampsPrompt0 = QLabel("Current video prompt timestamps (emergencies) for the trivial (with tasks) scenario:")
        self.emergencyTimestampsName = QLabel(",".join(self.INFO["emergencyTimestamps"]))
        self.emergencyTimestampsPrompt1 = QLabel("Enter new timestamps as a comma-separated list (no spaces):")
        self.emergencyTimestamps = QLineEdit()
        self.emergencyTimestampsPrompt1.setHidden(True)
        self.emergencyTimestamps.setHidden(True)
        timestampsLayout.addWidget(emergencyTimestampsPrompt0, 0, 1)
        timestampsLayout.addWidget(self.emergencyTimestampsName, 1, 1)
        timestampsLayout.addWidget(self.emergencyTimestampsPrompt1, 2, 1)
        timestampsLayout.addWidget(self.emergencyTimestamps, 3, 1)
        layout.addLayout(timestampsLayout, 2, 1)

        # module for setting the trivial button display time
        displayTimeLayout = QGridLayout()
        displayTimePrompt0 = QLabel("Current delay time for button display for the trivial (with tasks) scenario:")
        self.displayTimeName = QLabel(self.INFO["displayTime"])
        self.displayTimePrompt1 = QLabel("Enter new delay time (must be greater than the minimal interval in timestamps):")
        self.displayTime = QLineEdit()
        self.displayTimePrompt1.setHidden(True)
        self.displayTime.setHidden(True)
        displayTimeLayout.addWidget(displayTimePrompt0, 0, 0)
        displayTimeLayout.addWidget(self.displayTimeName, 1, 0)
        displayTimeLayout.addWidget(self.displayTimePrompt1, 2, 0)
        displayTimeLayout.addWidget(self.displayTime, 3, 0)
        layout.addLayout(displayTimeLayout, 2, 2)

        submitLayout = QGridLayout()
        self.editPrompt = QLabel("Press the Edit button to change settings.")
        self.editButton = QPushButton("Edit")
        self.submitPrompt = QLabel("Leave the textbox of fields you don't want to change blank. Press the Submit button to preserve changes.")
        self.submitButton = QPushButton("Submit")
        submitLayout.addWidget(self.editPrompt, 0, 0)
        submitLayout.addWidget(self.editButton, 1, 0)
        submitLayout.addWidget(self.submitPrompt, 0, 0)
        submitLayout.addWidget(self.submitButton, 1, 0)
        self.submitButton.setHidden(True)
        self.submitPrompt.setHidden(True)
        layout.addLayout(submitLayout, 3, 1, 1, 2)

        self.editButton.clicked.connect(self.editButtonClicked)
        self.submitButton.clicked.connect(self.submitButtonClicked)
        self.submitButton.clicked.connect(self.flushToFiles)
        
        self.setLayout(layout)
    
    def setChangeWindowButton(self, parentFunc):
        self.changeWindowButton.clicked.connect(parentFunc)

    def editButtonClicked(self):
        self.editButton.setHidden(True)
        self.editPrompt.setHidden(True)
        self.submitButton.setHidden(False)
        self.submitPrompt.setHidden(False)
        self.videoPrompt1.setHidden(False)
        self.video.setHidden(False)
        self.outputPrompt1.setHidden(False)
        self.output.setHidden(False)
        self.taskTimestampsPrompt1.setHidden(False)
        self.taskTimestamps.setHidden(False)
        self.emergencyTimestampsPrompt1.setHidden(False)
        self.emergencyTimestamps.setHidden(False)
        self.displayTimePrompt1.setHidden(False)
        self.displayTime.setHidden(False)

    def submitButtonClicked(self):
        self.editButton.setHidden(False)
        self.editPrompt.setHidden(False)
        self.submitButton.setHidden(True)
        self.submitPrompt.setHidden(True)
        self.videoPrompt1.setHidden(True)
        self.video.setHidden(True)
        self.outputPrompt1.setHidden(True)
        self.output.setHidden(True)
        self.taskTimestampsPrompt1.setHidden(True)
        self.taskTimestamps.setHidden(True)
        self.emergencyTimestampsPrompt1.setHidden(True)
        self.emergencyTimestamps.setHidden(True)
        self.displayTimePrompt1.setHidden(True)
        self.displayTime.setHidden(True)

    def flushToFiles(self):
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

        with open("./storage/trivialFiles.csv", "w", newline='') as writer:
                csv.writer(writer).writerow([self.INFO["videoName"], self.INFO["outputName"], self.INFO["displayTime"]])

        if (len(self.taskTimestamps.text()) > 0):
            self.INFO["taskTimestamps"] = self.taskTimestamps.text().split(",")
            self.taskTimestamps.clear()
            self.taskTimestampsName.setText(",".join(self.INFO["taskTimestamps"]))
            with open("./storage/trivialTaskTimes.csv", "w", newline='') as writer:
                csv.writer(writer).writerow(self.INFO["taskTimestamps"])
        
        if (len(self.emergencyTimestamps.text()) > 0):
            self.INFO["emergencyTimestamps"] = self.emergencyTimestamps.text().split(",")
            self.emergencyTimestamps.clear()
            self.emergencyTimestampsName.setText(",".join(self.INFO["emergencyTimestamps"]))
            with open("./storage/trivialemergencyTimes.csv", "w", newline='') as writer:
                csv.writer(writer).writerow(self.INFO["emergencyTimestamps"])