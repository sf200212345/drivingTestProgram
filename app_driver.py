from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QStackedLayout
from experiment_window import ExperimentWindow
from info_window import InfoWindow
from final_window import FinalWindow
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

            # cascade changes to initialization, fileNames, menu
            "displayTime": ""
        }
        self.initializeINFO()
        
        self.layout = QStackedLayout()

        # add all windows as class variables to use the window variables
        self.InfoWindow = InfoWindow(self.INFO)
        self.ExperimentWindow = ExperimentWindow(self.INFO)
        self.FinalWindow = FinalWindow(self.INFO)

        self.layout.addWidget(self.InfoWindow)
        self.layout.addWidget(self.ExperimentWindow)
        self.layout.addWidget(self.FinalWindow)
        self.layout.setCurrentIndex(0)
        self.setLayout(self.layout)

        # connect transition buttons to functions in WindowManager
        self.InfoWindow.setReadyButton(self.readyButtonClicked)
        self.InfoWindow.setReadyButton(self.ExperimentWindow.renderVideo)
        self.ExperimentWindow.setCompleteButton(self.completeButtonClicked)
        self.ExperimentWindow.setCompleteButton(self.FinalWindow.flushToCSV)
        self.FinalWindow.setReturnToStartButton(self.returnToStartButtonClicked)

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