from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QStackedLayout
from scripts.experiment_window import ExperimentWindow
from scripts.info_window import InfoWindow
from scripts.final_window import FinalWindow
import csv
import datetime

# Houses all windows
class WindowManager(QWidget):
    def __init__(self):
        super().__init__()
        
        self.INFO = {
            "output": [],
            "startTime": datetime.datetime.now(),
            "outputName": "",
            "videoName": "",
            "timestamps": [],
            "taskTimes": [],
            "displayTime": ""
        }

        self.scenario = ""

        self.initializeINFO()
        
        self.layout = QStackedLayout()

        # add all windows as class variables to use the window variables
        self.InfoWindow = InfoWindow(self.scenario)
        self.ExperimentWindow = ExperimentWindow(self.INFO, self.scenario)
        self.FinalWindow = FinalWindow(self.INFO)

        self.layout.addWidget(self.InfoWindow)
        self.layout.addWidget(self.ExperimentWindow)
        self.layout.addWidget(self.FinalWindow)
        self.layout.setCurrentIndex(0)
        self.setLayout(self.layout)

        # connect transition buttons to functions in WindowManager
        self.InfoWindow.setReadyButton(self.readyButtonClicked)
        if self.scenario == "C":
            self.InfoWindow.setReadyButton(self.ExperimentWindow.renderVideoControl)
        else:
            self.InfoWindow.setReadyButton(self.ExperimentWindow.renderVideoTrivial)
        self.ExperimentWindow.setCompleteButton(self.completeButtonClicked)
        self.ExperimentWindow.setCompleteButton(self.FinalWindow.flushToCSV)
        self.FinalWindow.setReturnToStartButton(self.returnToStartButtonClicked)

    def initializeINFO(self):
        with open("./storage/mode.csv", newline='') as fileName:
            reader = csv.reader(fileName)
            for row in reader:
                self.scenario = row[0]
        if self.scenario == "C":
            with open("./storage/controlFiles.csv", newline='') as fileName:
                reader = csv.reader(fileName)
                for row in reader:
                    self.INFO["videoName"] = row[0]
                    self.INFO["outputName"] = row[1]
                    self.INFO["displayTime"] = row[2]
            with open("./storage/controlTimes.csv", newline='') as fileName:
                reader = csv.reader(fileName)
                for row in reader:
                    self.INFO["timestamps"] = row
        else:
            with open("./storage/trivialFiles.csv", newline='') as fileName:
                reader = csv.reader(fileName)
                for row in reader:
                    self.INFO["videoName"] = row[0]
                    self.INFO["outputName"] = row[1]
                    self.INFO["displayTime"] = row[2]
            with open("./storage/trivialEmergencyTimes.csv", newline='') as fileName:
                reader = csv.reader(fileName)
                for row in reader:
                    self.INFO["timestamps"] = row
            with open("./storage/trivialTaskTimes.csv", newline='') as fileName:
                reader = csv.reader(fileName)
                for row in reader:
                    self.INFO["taskTimes"] = row

    def readyButtonClicked(self):
        self.layout.setCurrentIndex(1)
    
    def completeButtonClicked(self):
        self.layout.setCurrentIndex(2)

    def returnToStartButtonClicked(self):
        self.layout.setCurrentIndex(0)
        self.INFO["output"].clear()

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Autonomous Driving Experiment")
        self.WindowManager = WindowManager()
        self.setCentralWidget(self.WindowManager)
        self.showMaximized()

app = QApplication([])

window = MainWindow()
window.show()

app.exec()