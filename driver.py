from PyQt6.QtWidgets import QApplication, QMainWindow
from appWindows import WelcomeWindow, InfoWindow, ExperimentWindow, FinalWindow

# if the scenario is control: true
# if the scenario is trivial: false
CONTROL = True

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Automated Driving with/without Trivial Tasks Experiment")
        
        # control or trivial
        self.testScenario = CONTROL

        # add all windows as class variables to use the window variables
        self.WelcomeWindow = WelcomeWindow()
        self.InfoWindow = InfoWindow()
        self.ExperimentWindow = ExperimentWindow()
        self.FinalWindow = FinalWindow()

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
        self.ExperimentWindow.startVideo()
        self.setCentralWidget(self.ExperimentWindow)
    
    def complete_button_clicked(self):
        self.FinalWindow.flushToCSV(self.testScenario)
        self.setCentralWidget(self.FinalWindow)


app = QApplication([])

window = MainWindow()
window.show()

app.exec()