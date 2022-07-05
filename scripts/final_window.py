from PyQt6.QtWidgets import QLabel, QGridLayout, QWidget, QPushButton
import csv

'''
Displays a "finished" screen
Processes data collected from ExperimentWindow
Flushes results to csv file
'''
class FinalWindow(QWidget):
    def __init__(self, INFO):
        super().__init__()
    
        self.INFO = INFO
        self.timestamps = self.INFO["taskTimes"] + self.INFO["timestamps"]
        for i in range(len(self.timestamps)):
            self.timestamps[i] = float(self.timestamps[i])
        self.timestamps.sort()
        layout = QGridLayout()

        layout.addWidget(QLabel("Finished! Press the button below to conduct another experiment. Close the window to end the experiment."), 1, 1, 2, 2)

        self.returnToStartButton = QPushButton("Return to Start")
        layout.addWidget(self.returnToStartButton, 2, 1, 1, 2)
        layout.addWidget(QWidget(), 0, 3)
        layout.addWidget(QWidget(), 3, 0)
        self.setLayout(layout)
        
    def flushToCSV(self):
        if len(self.INFO["output"]) != len(self.timestamps):
            self.INFO["output"] = ["I", "Invalid Data: Number of button-presses must equal the number of prompts (tasks/emergencies) in video."]
        else:
            for i in range(len(self.INFO["output"])):
                self.INFO["output"][i] = (self.INFO["output"][i] - self.INFO["startTime"]).total_seconds() - self.timestamps[i]
        with open(self.INFO["outputName"], "a", newline='') as writer:
            csv.writer(writer).writerow(self.INFO["output"])

    def setReturnToStartButton(self, parentFunc):
        self.returnToStartButton.clicked.connect(parentFunc)