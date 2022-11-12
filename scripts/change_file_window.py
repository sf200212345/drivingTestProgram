from PyQt6.QtWidgets import QWidget, QGridLayout, QLabel, QLineEdit, QPushButton
from PyQt6.QtCore import Qt
import csv

class ChangeFileWindowControl(QWidget):
    def __init__(self, CINFO):
        super().__init__()

        self.INFO = CINFO
        layout = QGridLayout()

        self.changeWindowButton = QPushButton("Current Mode: Control\nPress to switch")
        self.changeWindowButton.setObjectName("changeWindowButton")
        layout.addWidget(self.changeWindowButton, 0, 0)

        # module for setting the control video name
        videoLayout = QGridLayout()
        videoPrompt0 = QLabel("Current video name for the control (no tasks) scenario:")
        videoPrompt0.setObjectName("bold")
        self.videoName = QLabel(self.INFO["videoName"])
        self.videoName.setTextInteractionFlags(Qt.TextInteractionFlag.TextSelectableByMouse)
        self.videoPrompt1 = QLabel("Enter new video name (including file extension):")
        self.video = QLineEdit()
        self.videoPrompt1.setHidden(True)
        self.video.setHidden(True)
        videoLayout.addWidget(videoPrompt0, 0, 0)
        videoLayout.addWidget(self.videoName, 1, 0)
        videoLayout.addWidget(self.videoPrompt1, 2, 0)
        videoLayout.addWidget(self.video, 3, 0)
        layout.addLayout(videoLayout, 0, 1)

        # module for setting the control output file name
        outputLayout = QGridLayout()
        outputPrompt0 = QLabel("Current output file name for the control (no tasks) scenario:")
        outputPrompt0.setObjectName("bold")
        self.outputName = QLabel(self.INFO["outputName"])
        self.outputName.setTextInteractionFlags(Qt.TextInteractionFlag.TextSelectableByMouse)
        self.outputPrompt1 = QLabel("Enter new output file name (including file extension):")
        self.output = QLineEdit()
        self.outputPrompt1.setHidden(True)
        self.output.setHidden(True)
        outputLayout.addWidget(outputPrompt0, 0, 0)
        outputLayout.addWidget(self.outputName, 1, 0)
        outputLayout.addWidget(self.outputPrompt1, 2, 0)
        outputLayout.addWidget(self.output, 3, 0)
        layout.addLayout(outputLayout, 0, 2)

        # module for setting the control video timestamps
        timestampsLayout = QGridLayout()
        timestampsPrompt0 = QLabel("Current video prompt timestamps (emergencies) for the control (no tasks) scenario:\nEither seconds or MM:SS:MS format are acceptable.")
        timestampsPrompt0.setObjectName("bold")
        self.timestampsName = QLabel(",".join(self.INFO["timestamps"]))
        self.timestampsName.setTextInteractionFlags(Qt.TextInteractionFlag.TextSelectableByMouse)
        self.timestampsPrompt1 = QLabel("Enter new timestamps as a comma-separated list:")
        self.timestamps = QLineEdit()
        self.timestampsPrompt1.setHidden(True)
        self.timestamps.setHidden(True)
        timestampsLayout.addWidget(timestampsPrompt0, 0, 0)
        timestampsLayout.addWidget(self.timestampsName, 1, 0)
        timestampsLayout.addWidget(self.timestampsPrompt1, 2, 0)
        timestampsLayout.addWidget(self.timestamps, 3, 0)
        layout.addLayout(timestampsLayout, 1, 2)

        # module for setting the control button display time
        displayTimeLayout = QGridLayout()
        displayTimePrompt0 = QLabel("Current delay time for button display for the control (no tasks) scenario:\nPlease only enter a single number.")
        displayTimePrompt0.setObjectName("bold")
        self.displayTimeName = QLabel(self.INFO["displayTime"])
        self.displayTimeName.setTextInteractionFlags(Qt.TextInteractionFlag.TextSelectableByMouse)
        self.displayTimePrompt1 = QLabel("Enter new delay time in SECONDS (must be less than the minimal interval in timestamps):")
        self.displayTime = QLineEdit()
        self.displayTimePrompt1.setHidden(True)
        self.displayTime.setHidden(True)
        displayTimeLayout.addWidget(displayTimePrompt0, 0, 0)
        displayTimeLayout.addWidget(self.displayTimeName, 1, 0)
        displayTimeLayout.addWidget(self.displayTimePrompt1, 2, 0)
        displayTimeLayout.addWidget(self.displayTime, 3, 0)
        layout.addLayout(displayTimeLayout, 2, 1)

        # module for setting the control survey link
        surveyLinkLayout = QGridLayout()
        surveyLinkPrompt0 = QLabel("Current survey link for the control (no tasks) scenario:")
        surveyLinkPrompt0.setObjectName("bold")
        self.surveyLinkName = QLabel(self.INFO["surveyLink"])
        self.surveyLinkName.setTextInteractionFlags(Qt.TextInteractionFlag.TextSelectableByMouse)
        self.surveyLinkName.setWordWrap(True)
        self.surveyLinkPrompt1 = QLabel("Enter new survey link:")
        self.surveyLink = QLineEdit()
        self.surveyLinkPrompt1.setHidden(True)
        self.surveyLink.setHidden(True)
        surveyLinkLayout.addWidget(surveyLinkPrompt0, 0, 0)
        surveyLinkLayout.addWidget(self.surveyLinkName, 1, 0)
        surveyLinkLayout.addWidget(self.surveyLinkPrompt1, 2, 0)
        surveyLinkLayout.addWidget(self.surveyLink, 3, 0)
        layout.addLayout(surveyLinkLayout, 2, 2)

        submitLayout = QGridLayout()
        self.editPrompt = QLabel("Press the Edit button to change settings.")
        self.editPrompt.setObjectName("bold")
        self.editButton = QPushButton("Edit")
        self.submitPrompt = QLabel("Leave the textbox of fields you don't want to change blank.\nPress the Submit button to preserve changes.")
        self.submitPrompt.setObjectName("bold")
        self.submitButton = QPushButton("Submit")
        self.editButton.setObjectName("edit-btn")
        self.submitButton.setObjectName("sbt-btn")
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
        self.surveyLinkPrompt1.setHidden(False)
        self.surveyLink.setHidden(False)

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
        self.surveyLinkPrompt1.setHidden(True)
        self.surveyLink.setHidden(True)

    def flushToFiles(self):
        if (len(self.video.text()) > 0):
            self.INFO["videoName"] = self.video.text().strip()
            self.video.clear()
            self.videoName.setText(self.INFO["videoName"])

        if (len(self.output.text()) > 0):
            self.INFO["outputName"] = self.output.text().strip()
            self.output.clear()
            self.outputName.setText(self.INFO["outputName"])

        if (len(self.displayTime.text()) > 0):
            self.INFO["displayTime"] = self.displayTime.text().strip()
            self.displayTime.clear()
            self.displayTimeName.setText(self.INFO["displayTime"])

        if (len(self.surveyLink.text()) > 0):
            self.INFO["surveyLink"] = self.surveyLink.text().strip()
            self.surveyLink.clear()
            self.surveyLinkName.setText(self.INFO["surveyLink"])

        with open("./storage/controlFiles.csv", "w", newline='') as writer:
            csv.writer(writer).writerow([self.INFO["videoName"], self.INFO["outputName"], self.INFO["displayTime"], self.INFO["surveyLink"]])

        if (len(self.timestamps.text()) > 0):
            self.INFO["timestamps"] = [time.strip() for time in self.timestamps.text().split(",")]
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
        self.changeWindowButton.setObjectName("changeWindowButton")
        layout.addWidget(self.changeWindowButton, 0, 0)

        # module for setting the trivial video name
        videoLayout = QGridLayout()
        videoPrompt0 = QLabel("Current video name for the trivial (with tasks) scenario:")
        videoPrompt0.setObjectName("bold")
        self.videoName = QLabel(self.INFO["videoName"])
        self.videoName.setTextInteractionFlags(Qt.TextInteractionFlag.TextSelectableByMouse)
        self.videoPrompt1 = QLabel("Enter new video name (including file extension):")
        self.video = QLineEdit()
        self.videoPrompt1.setHidden(True)
        self.video.setHidden(True)
        videoLayout.addWidget(videoPrompt0, 0, 0)
        videoLayout.addWidget(self.videoName, 1, 0)
        videoLayout.addWidget(self.videoPrompt1, 2, 0)
        videoLayout.addWidget(self.video, 3, 0)
        layout.addLayout(videoLayout, 0, 1)

        # module for setting the trival output file name
        outputLayout = QGridLayout()
        outputPrompt0 = QLabel("Current output file name for the trivial (with tasks) scenario:")
        outputPrompt0.setObjectName("bold")
        self.outputName = QLabel(self.INFO["outputName"])
        self.outputName.setTextInteractionFlags(Qt.TextInteractionFlag.TextSelectableByMouse)
        self.outputPrompt1 = QLabel("Enter new output file name (including file extension):")
        self.output = QLineEdit()
        self.outputPrompt1.setHidden(True)
        self.output.setHidden(True)
        outputLayout.addWidget(outputPrompt0, 0, 0)
        outputLayout.addWidget(self.outputName, 1, 0)
        outputLayout.addWidget(self.outputPrompt1, 2, 0)
        outputLayout.addWidget(self.output, 3, 0)
        layout.addLayout(outputLayout, 0, 2)

        # module for setting the trivial video task timestamps
        timestampsLayout = QGridLayout()
        taskTimestampsPrompt0 = QLabel("Current video prompt timestamps (tasks) for the trivial (with tasks) scenario:\nEither seconds or MM:SS:MS format are acceptable.")
        taskTimestampsPrompt0.setObjectName("bold")
        self.taskTimestampsName = QLabel(",".join(self.INFO["taskTimestamps"]))
        self.taskTimestampsName.setTextInteractionFlags(Qt.TextInteractionFlag.TextSelectableByMouse)
        self.taskTimestampsPrompt1 = QLabel("Enter new timestamps as a comma-separated list:")
        self.taskTimestamps = QLineEdit()
        self.taskTimestampsPrompt1.setHidden(True)
        self.taskTimestamps.setHidden(True)
        timestampsLayout.addWidget(taskTimestampsPrompt0, 0, 0)
        timestampsLayout.addWidget(self.taskTimestampsName, 1, 0)
        timestampsLayout.addWidget(self.taskTimestampsPrompt1, 2, 0)
        timestampsLayout.addWidget(self.taskTimestamps, 3, 0)
        layout.addLayout(timestampsLayout, 1, 1)

        # module for setting the trivial video emergency timestamps
        timestampsLayout1 = QGridLayout()
        emergencyTimestampsPrompt0 = QLabel("Current video prompt timestamps (emergencies) for the trivial (with tasks) scenario:\nEither seconds or MM:SS:MS format are acceptable.")
        emergencyTimestampsPrompt0.setObjectName("bold")
        self.emergencyTimestampsName = QLabel(",".join(self.INFO["emergencyTimestamps"]))
        self.emergencyTimestampsName.setTextInteractionFlags(Qt.TextInteractionFlag.TextSelectableByMouse)
        self.emergencyTimestampsPrompt1 = QLabel("Enter new timestamps as a comma-separated list:")
        self.emergencyTimestamps = QLineEdit()
        self.emergencyTimestampsPrompt1.setHidden(True)
        self.emergencyTimestamps.setHidden(True)
        timestampsLayout1.addWidget(emergencyTimestampsPrompt0, 0, 0)
        timestampsLayout1.addWidget(self.emergencyTimestampsName, 1, 0)
        timestampsLayout1.addWidget(self.emergencyTimestampsPrompt1, 2, 0)
        timestampsLayout1.addWidget(self.emergencyTimestamps, 3, 0)
        layout.addLayout(timestampsLayout1, 1, 2)

        # module for setting the trivial button display time
        displayTimeLayout = QGridLayout()
        displayTimePrompt0 = QLabel("Current delay time for button display for the trivial (with tasks) scenario:\nPlease only enter a single number.")
        displayTimePrompt0.setObjectName("bold")
        self.displayTimeName = QLabel(self.INFO["displayTime"])
        self.displayTimeName.setTextInteractionFlags(Qt.TextInteractionFlag.TextSelectableByMouse)
        self.displayTimePrompt1 = QLabel("Enter new delay time in SECONDS (must be less than the minimal interval in timestamps):")
        self.displayTime = QLineEdit()
        self.displayTimePrompt1.setHidden(True)
        self.displayTime.setHidden(True)
        displayTimeLayout.addWidget(displayTimePrompt0, 0, 0)
        displayTimeLayout.addWidget(self.displayTimeName, 1, 0)
        displayTimeLayout.addWidget(self.displayTimePrompt1, 2, 0)
        displayTimeLayout.addWidget(self.displayTime, 3, 0)
        layout.addLayout(displayTimeLayout, 2, 1)

        # module for setting the trivial survey link
        surveyLinkLayout = QGridLayout()
        surveyLinkPrompt0 = QLabel("Current survey link for the trivial (with tasks) scenario:")
        surveyLinkPrompt0.setObjectName("bold")
        self.surveyLinkName = QLabel(self.INFO["surveyLink"])
        self.surveyLinkName.setTextInteractionFlags(Qt.TextInteractionFlag.TextSelectableByMouse)
        self.surveyLinkName.setWordWrap(True)
        self.surveyLinkPrompt1 = QLabel("Enter new survey link:")
        self.surveyLink = QLineEdit()
        self.surveyLinkPrompt1.setHidden(True)
        self.surveyLink.setHidden(True)
        surveyLinkLayout.addWidget(surveyLinkPrompt0, 0, 0)
        surveyLinkLayout.addWidget(self.surveyLinkName, 1, 0)
        surveyLinkLayout.addWidget(self.surveyLinkPrompt1, 2, 0)
        surveyLinkLayout.addWidget(self.surveyLink, 3, 0)
        layout.addLayout(surveyLinkLayout, 2, 2)

        submitLayout = QGridLayout()
        self.editPrompt = QLabel("Press the Edit button to change settings.")
        self.editPrompt.setObjectName("bold")
        self.editButton = QPushButton("Edit")
        self.submitPrompt = QLabel("Leave the textbox of fields you don't want to change blank.\nPress the Submit button to preserve changes.")
        self.submitPrompt.setObjectName("bold")
        self.submitButton = QPushButton("Submit")
        self.editButton.setObjectName("edit-btn")
        self.submitButton.setObjectName("sbt-btn")
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
        self.surveyLinkPrompt1.setHidden(False)
        self.surveyLink.setHidden(False)

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
        self.surveyLinkPrompt1.setHidden(True)
        self.surveyLink.setHidden(True)

    def flushToFiles(self):
        if (len(self.video.text()) > 0):
            self.INFO["videoName"] = self.video.text().strip()
            self.video.clear()
            self.videoName.setText(self.INFO["videoName"])

        if (len(self.output.text()) > 0):
            self.INFO["outputName"] = self.output.text().strip()
            self.output.clear()
            self.outputName.setText(self.INFO["outputName"])

        if (len(self.displayTime.text()) > 0):
            self.INFO["displayTime"] = self.displayTime.text().strip()
            self.displayTime.clear()
            self.displayTimeName.setText(self.INFO["displayTime"])

        if (len(self.surveyLink.text()) > 0):
            self.INFO["surveyLink"] = self.surveyLink.text().strip()
            self.surveyLink.clear()
            self.surveyLinkName.setText(self.INFO["surveyLink"])

        with open("./storage/trivialFiles.csv", "w", newline='') as writer:
            csv.writer(writer).writerow([self.INFO["videoName"], self.INFO["outputName"], self.INFO["displayTime"], self.INFO["surveyLink"]])

        if (len(self.taskTimestamps.text()) > 0):
            self.INFO["taskTimestamps"] = [time.strip() for time in self.taskTimestamps.text().split(",")]
            self.taskTimestamps.clear()
            self.taskTimestampsName.setText(",".join(self.INFO["taskTimestamps"]))
            with open("./storage/trivialTaskTimes.csv", "w", newline='') as writer:
                csv.writer(writer).writerow(self.INFO["taskTimestamps"])
        
        if (len(self.emergencyTimestamps.text()) > 0):
            self.INFO["emergencyTimestamps"] = [time.strip() for time in self.emergencyTimestamps.text().split(",")]
            self.emergencyTimestamps.clear()
            self.emergencyTimestampsName.setText(",".join(self.INFO["emergencyTimestamps"]))
            with open("./storage/trivialemergencyTimes.csv", "w", newline='') as writer:
                csv.writer(writer).writerow(self.INFO["emergencyTimestamps"])