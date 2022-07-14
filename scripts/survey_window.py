from PyQt6.QtWidgets import QLabel, QGridLayout, QWidget, QPushButton, QLineEdit

'''
Prompts the user to enter the participantID and then submit
Appears after clicking on the button to open the survey website
'''
class SurveyWindow(QWidget):
    def __init__(self, INFO):
        super().__init__()
        
        self.INFO = INFO
        layout = QGridLayout()

        iDInstructions = QLabel('Please enter your participant ID here:')
        self.participantID = QLineEdit()
        self.submitButton = QPushButton("Submit")
        
        iDInstructions.setObjectName("iDInstructions")
        self.participantID.setObjectName("participantID")
        self.submitButton.setObjectName("submitButton")

        layout.addWidget(iDInstructions, 1, 1, 1, 2)
        layout.addWidget(self.participantID, 2, 1, 1, 2)
        layout.addWidget(self.submitButton, 3, 1, 1, 2)
        layout.addWidget(QWidget(), 0, 3)
        layout.addWidget(QWidget(), 3, 0)

        self.setLayout(layout)

        self.submitButton.clicked.connect(self.submitParticipantID)

    def setSubmitButton(self, parentFunc):
        self.submitButton.clicked.connect(parentFunc)

    def submitParticipantID(self):
        self.INFO["participantID"] = self.participantID.text()
    #make new function to validate the participant id