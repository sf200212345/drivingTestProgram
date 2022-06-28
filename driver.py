from PyQt6.QtWidgets import QApplication, QMainWindow
from appWindows import WelcomeWindow, InfoWindow, ExperimentWindow, FinalWindow
import csv

# if the scenario is control: true
# if the scenario is trivial: false
CONTROL = True

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Automated Driving with/without Trivial Tasks Experiment")
        
        self.INFO = {
            "output": []
        }
        self.initializeINFO()

        # control or trivial
        self.testScenario = CONTROL

        # add all windows as class variables to use the window variables
        self.WelcomeWindow = WelcomeWindow(self.INFO)
        self.InfoWindow = InfoWindow()
        self.ExperimentWindow = ExperimentWindow(self.INFO)
        self.FinalWindow = FinalWindow(self.INFO)

        # connect transition buttons to functions in MainWindow
        self.WelcomeWindow.setControlButton(self.control_button_clicked)
        self.WelcomeWindow.setTrivialButton(self.trivial_button_clicked)
        self.InfoWindow.setReadyButton(self.ready_button_clicked)
        self.ExperimentWindow.setCompleteButton(self.complete_button_clicked)

        self.setCentralWidget(self.WelcomeWindow)
    
    def control_button_clicked(self):
        self.testScenario = CONTROL
        self.InfoWindow.renderOnScenario(self.testScenario)
        self.ExperimentWindow.renderOnScenario(self.testScenario)
        self.setCentralWidget(self.InfoWindow)
    
    def trivial_button_clicked(self):
        self.testScenario = not CONTROL
        self.InfoWindow.renderOnScenario(self.testScenario)
        self.ExperimentWindow.renderOnScenario(self.testScenario)
        self.setCentralWidget(self.InfoWindow)

    def ready_button_clicked(self):
        self.setCentralWidget(self.ExperimentWindow)
        self.ExperimentWindow.startVideo()
    
    def complete_button_clicked(self):
        self.ExperimentWindow.stopVideo()
        self.FinalWindow.flushToCSV(self.testScenario)
        self.setCentralWidget(self.FinalWindow)

    def initializeINFO(self):
        with open("fileNames.csv", newline='') as fileName:
            reader = csv.reader(fileName)
            for row in reader:
                self.INFO["controlVideo"] = row[0]
                self.INFO["trivialVideo"] = row[1]
                self.INFO["controlFileName"] = row[2]
                self.INFO["trivialFileName"] = row[3]
                with open(row[4], newline='') as controlTimes:
                    controlReader = csv.reader(controlTimes)
                    for i in controlReader:
                        self.INFO["controlTimes"] = i
                with open(row[5], newline='') as trivialTimes:
                    trivialReader = csv.reader(trivialTimes)
                    for j in trivialReader:
                        self.INFO["trivialTimes"] = j

app = QApplication([])

window = MainWindow()
window.show()

app.exec()