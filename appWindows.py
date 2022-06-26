from PyQt6.QtWidgets import QLabel, QGridLayout, QWidget, QPushButton
import datetime
import csv

OUTPUT = []
'''
First window you see when starting up the app
Has a title and two buttons
controlButton leads to the video without trivial tasks
trivialButton leads to the video with trivial tasks
'''
class WelcomeWindow(QWidget):
    def __init__(self):
        super().__init__()

        layout = QGridLayout()

        layout.addWidget(QLabel("Welcome! Press one of the buttons below to get started."), 1, 1, 1, 2)
        self.controlButton = QPushButton("Control")
        self.trivialButton = QPushButton("Trivial Tasks")
        layout.addWidget(self.controlButton, 2, 1)
        layout.addWidget(self.trivialButton, 2, 2)
        layout.addWidget(QWidget(), 0, 3)
        layout.addWidget(QWidget(), 3, 0)
        self.setLayout(layout)
    
    def setControlButton(self, parentFunc):
        self.controlButton.clicked.connect(parentFunc)

    def setTrivialButton(self, parentFunc):
        self.trivialButton.clicked.connect(parentFunc)
        
'''
Tells the user what to do in the incoming experiment
Has an "I'm ready" button to start
'''
class InfoWindow(QWidget):
    def __init__(self):
        super().__init__()

        layout = QGridLayout()

        self.instructions = QLabel()
        layout.addWidget(self.instructions, 1, 1, 1, 2)
        self.readyButton = QPushButton("Ready")
        layout.addWidget(self.readyButton, 2, 1, 1, 2)
        layout.addWidget(QWidget(), 0, 3)
        layout.addWidget(QWidget(), 3, 0)
        self.setLayout(layout)
    
    def renderOnScenario(self, scenario):
        if scenario:
            self.instructions.setText("Instructions for control scenario")
        else:
            self.instructions.setText("Instructions for trivial scenario")

    def setReadyButton(self, parentFunc):
        self.readyButton.clicked.connect(parentFunc)

'''
Displays the video and two/one buttons to press depending on the selected scenario
Create self.dict with times as the key, upon reading the timestamp record the time
Upon button press record the time again, store the difference between times as csv string
'''
class ExperimentWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.startTime = datetime.datetime.now()

        layout = QGridLayout()

        self.taskButton = QPushButton("start time")
        self.emergencyButton = QPushButton("stop time")
        self.longTaskButton = QPushButton("Do Task")
        self.completeButton = QPushButton("Complete")
        layout.addWidget(self.taskButton, 1, 1)
        layout.addWidget(self.emergencyButton, 1, 2)
        layout.addWidget(self.longTaskButton, 1, 1, 1, 2)
        layout.addWidget(self.completeButton, 2, 1, 1, 2)
        layout.addWidget(QWidget(), 0, 3)
        layout.addWidget(QWidget(), 3, 0)
        self.setLayout(layout)

        self.taskButton.clicked.connect(self.taskButtonClicked)
        self.emergencyButton.clicked.connect(self.emergencyButtonClicked)
    
    def renderOnScenario(self, scenario):
        if scenario:
            self.taskButton.setHidden(True)
            self.emergencyButton.setHidden(True)
        else:
            self.longTaskButton.setHidden(True)

    def setCompleteButton(self, parentFunc):
        self.completeButton.clicked.connect(parentFunc)

    def taskButtonClicked(self):
        self.startTime = datetime.datetime.now()
    
    def emergencyButtonClicked(self):
        OUTPUT.append((datetime.datetime.now() - self.startTime).total_seconds())

'''
Displays a "finished" screen
Flushes results to csv file
Give option to go back to WelcomeWindow
'''
class FinalWindow(QWidget):
    def __init__(self):
        super().__init__()

        layout = QGridLayout()

        layout.addWidget(QLabel("Finished! Close the window."), 1, 1, 2, 2)
        layout.addWidget(QWidget(), 0, 3)
        layout.addWidget(QWidget(), 3, 0)
        self.setLayout(layout)

    def flushToCSV(self, scenario):
        if scenario:
            with open("controlResults.csv", "a", newline='') as writer:
                csv.writer(writer).writerow(OUTPUT)
        else:
            with open("trivialTasksResults.csv", "a", newline='') as writer:
                csv.writer(writer).writerow(OUTPUT)
