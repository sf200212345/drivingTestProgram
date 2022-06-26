from PyQt6.QtWidgets import QApplication, QLabel, QMainWindow, QGridLayout, QWidget, QPushButton
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
        controlButton = QPushButton("Control")
        trivialButton = QPushButton("Trivial Tasks")
        layout.addWidget(controlButton, 2, 1)
        layout.addWidget(trivialButton, 2, 2)
        layout.addWidget(QWidget(), 0, 3)
        layout.addWidget(QWidget(), 3, 0)
        self.setLayout(layout)
        # add handlers to change displays upon pressing the button
        # don't forget to bind the signals to the slots
        
'''
Tells the user what to do in the incoming experiment
Has an "I'm ready" button to start
'''
class InfoWindow(QWidget):
    def __init__(self):
        super().__init__()

        layout = QGridLayout()

'''
Displays the video and two/one buttons to press depending on the selected scenario
Create self.dict with times as the key, upon reading the timestamp record the time
Upon button press record the time again, store the difference between times as csv string
'''
class ExperimentWindow(QWidget):
    # might have to pass another value here to choose the scenario
    def __init__(self):
        super().__init__()

        layout = QGridLayout()

'''
Displays a "finished" screen
Flushes results to csv file
Give option to go back to WelcomeWindow
'''
class FinalWindow(QWidget):
    def __init__(self):
        super().__init__()

        layout = QGridLayout()

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Automated Driving with/without Trivial Tasks Experiment")
        self.setCentralWidget(WelcomeWindow())


app = QApplication([])

window = MainWindow()
window.show()

app.exec()