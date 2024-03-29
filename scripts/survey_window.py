from PyQt6.QtWidgets import QLabel, QGridLayout, QWidget, QPushButton, QLineEdit, QTextEdit
import webbrowser
import time

'''
Prompts the user to enter the participantID and then submit
Appears after clicking on the button to open the survey website
'''
class SurveyWindow(QWidget):
    def __init__(self, INFO, submitButtonClicked, flushToCSV):
        super().__init__()
        
        self.clicked = submitButtonClicked
        self.flush = flushToCSV
        self.INFO = INFO

        layout = QGridLayout()

        self.surveyInstructions = QTextEdit()
        self.surveyInstructions.setHtml(
            '''
            <div style="text-align: center">
                Please press the button below to open the survey.
                Make sure to remember your participant ID.
            </div>
            '''
        )
        self.surveyInstructions.setReadOnly(True)
        
        self.surveyButton = QPushButton("Open Survey")

        self.iDInstructions = QLabel('Please enter your participant ID here:')
        self.participantID = QLineEdit()
        self.submitButton = QPushButton("Submit")
        self.validationPrompt = QLabel()
        
        self.surveyInstructions.setObjectName("surveyInstructions")
        self.surveyButton.setObjectName("surveyButton")
        self.iDInstructions.setObjectName("iDInstructions")
        self.participantID.setObjectName("participantID")
        self.submitButton.setObjectName("submitButton")
        self.validationPrompt.setObjectName("validationPrompt")

        layout.addWidget(self.surveyInstructions, 1, 1, 1, 2)
        layout.addWidget(self.surveyButton, 2, 1, 1, 2)

        inputLayout = QGridLayout()
        inputLayout.addWidget(self.iDInstructions, 0, 0, 1, 2)
        inputLayout.addWidget(self.participantID, 1, 0, 1, 2)

        submitLayout = QGridLayout()
        submitLayout.addWidget(self.validationPrompt, 0, 0, 1, 2)
        submitLayout.addWidget(self.submitButton, 1, 0, 1, 2)

        self.iDInstructions.setHidden(True)
        self.participantID.setHidden(True)
        self.validationPrompt.setHidden(True)
        self.submitButton.setHidden(True)

        layout.addLayout(inputLayout, 1, 1, 1, 2)
        layout.addLayout(submitLayout, 2, 1, 1, 2)
        layout.addWidget(QWidget(), 0, 3)
        layout.addWidget(QWidget(), 3, 0)

        self.setLayout(layout)

        self.surveyButton.clicked.connect(self.surveyButtonClicked)
        self.submitButton.clicked.connect(self.submitParticipantID)

    def submitParticipantID(self):
        if len(self.participantID.text()) == 0:
            self.validationPrompt.setText("*You cannot leave this field empty.")
        elif not self.participantID.text().isnumeric():
            self.validationPrompt.setText("*Your participant ID must consist only of numbers (0-9). There should be no whitespace, letters or special characters.")
        else:
            self.INFO["participantID"] = self.participantID.text()
            self.flush()
            self.clicked()
    
    def surveyButtonClicked(self):
        webbrowser.open_new(self.INFO["surveyLink"])
        time.sleep(5)
        self.surveyInstructions.setHidden(True)
        self.surveyButton.setHidden(True)
        self.iDInstructions.setHidden(False)
        self.participantID.setHidden(False)
        self.validationPrompt.setHidden(False)
        self.submitButton.setHidden(False)
        