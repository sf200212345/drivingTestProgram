from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout, QLabel, QLineEdit, QPushButton
import csv

# Houses all windows
class EditWindow(QWidget):
    def __init__(self):
        super().__init__()
        
        self.INFO = {
            "output": [],
            "outputName": "",
            "videoName": "",
            "timestamps": [],

            # cascade changes to initialization, fileNames, menu
            "displayTime": ""
        }
        self.initializeINFO()
        
        layout = QGridLayout()

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

    def initializeINFO(self):
        with open("fileInfo.csv", newline='') as fileName:
            reader = csv.reader(fileName)
            for row in reader:
                self.INFO["videoName"] = row[0]
                self.INFO["outputName"] = row[1]
                with open(row[2], newline='') as controlTimes:
                    reader = csv.reader(controlTimes)
                    for i in reader:
                        self.INFO["timestamps"] = i
                self.INFO["displayTime"] = row[3]

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Settings")
        self.EditWindow = EditWindow()
        self.setCentralWidget(self.EditWindow)
        self.showMaximized()

app = QApplication([])

window = MainWindow()
window.show()

app.exec()