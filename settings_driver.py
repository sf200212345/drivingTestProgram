from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QStackedLayout
from scripts.change_file_window import ChangeFileWindowControl, ChangeFileWindowTrivial
import csv

# Houses all windows
class EditWindow(QWidget):
    def __init__(self):
        super().__init__()
        
        self.CINFO = {
            "outputName": "",
            "videoName": "",
            "timestamps": [],
            "displayTime": ""
        }
        
        self.TINFO = {
            "outputName": "",
            "videoName": "",
            "taskTimestamps": [],
            "emergencyTimestamps": [],
            "displayTime": ""
        }

        self.scenario = ""

        self.initializeINFO()

        self.layout = QStackedLayout()

        self.ChangeFileWindowControl = ChangeFileWindowControl(self.CINFO)
        self.ChangeFileWindowTrivial = ChangeFileWindowTrivial(self.TINFO)

        self.layout.addWidget(self.ChangeFileWindowControl)
        self.layout.addWidget(self.ChangeFileWindowTrivial)

        if self.scenario == "C":
            self.layout.setCurrentIndex(0)
        else:
            self.layout.setCurrentIndex(1)
        
        self.ChangeFileWindowControl.setChangeWindowButton(self.changeWindowButtonClicked)
        self.ChangeFileWindowTrivial.setChangeWindowButton(self.changeWindowButtonClicked)

        self.setLayout(self.layout)
        
    def initializeINFO(self):
        with open("./storage/mode.csv", newline='') as fileName:
            reader = csv.reader(fileName)
            for row in reader:
                self.scenario = row[0]
        with open("./storage/controlFiles.csv", newline='') as fileName:
            reader = csv.reader(fileName)
            for row in reader:
                self.CINFO["videoName"] = row[0]
                self.CINFO["outputName"] = row[1]
                self.CINFO["displayTime"] = row[2]
        with open("./storage/controlTimes.csv", newline='') as fileName:
            reader = csv.reader(fileName)
            for row in reader:
                self.CINFO["timestamps"] = row
        
        with open("./storage/trivialFiles.csv", newline='') as fileName:
            reader = csv.reader(fileName)
            for row in reader:
                self.TINFO["videoName"] = row[0]
                self.TINFO["outputName"] = row[1]
                self.TINFO["displayTime"] = row[2]
        with open("./storage/trivialTaskTimes.csv", newline='') as fileName:
            reader = csv.reader(fileName)
            for row in reader:
                self.TINFO["taskTimestamps"] = row
        with open("./storage/trivialEmergencyTimes.csv", newline='') as fileName:
            reader = csv.reader(fileName)
            for row in reader:
                self.TINFO["emergencyTimestamps"] = row
        

    def changeWindowButtonClicked(self):
        if self.scenario == "C":
            self.scenario = "T"
            self.layout.setCurrentIndex(1)
        else:
            self.scenario = "C"
            self.layout.setCurrentIndex(0)
        with open("./storage/mode.csv", "w", newline='') as writer:
                csv.writer(writer).writerow([self.scenario])

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Settings")
        self.EditWindow = EditWindow()
        self.setCentralWidget(self.EditWindow)
        self.showMaximized()

app = QApplication([])

with open("./styles/settings_styles.css", 'r') as f:
    style = f.read()
    app.setStyleSheet(style)

window = MainWindow()
window.show()

app.exec()