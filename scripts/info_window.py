from PyQt6.QtWidgets import QLabel, QGridLayout, QWidget, QPushButton

'''
Tells the user what to do in the incoming experiment
Has a settings button that allows the experiment operator to change file names and times
Has an "I'm ready" button to start
'''
class InfoWindow(QWidget):
    def __init__(self, scenario):
        super().__init__()
        
        layout = QGridLayout()

        instructions = QLabel('Instructions for control scenario:\nPress the "Emergency" button when an emergency situation arises.')
        self.readyButton = QPushButton("Ready")
        
        if scenario != "C":
            instructions.setText('Instructions for trivial scenario:\nPress the "Do Task" button when prompted. Press the "Emergency" button when an emergency situation arises.')
        
        instructions.setObjectName("instructions")
        self.readyButton.setObjectName("readyButton")

        layout.addWidget(instructions, 1, 1, 1, 2)
        layout.addWidget(self.readyButton, 2, 1, 1, 2)
        layout.addWidget(QWidget(), 0, 3)
        layout.addWidget(QWidget(), 3, 0)

        self.setLayout(layout)

    def setReadyButton(self, parentFunc):
        self.readyButton.clicked.connect(parentFunc)