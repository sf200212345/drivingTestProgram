from PyQt6.QtWidgets import QGridLayout, QWidget, QPushButton, QTextEdit

'''
Tells the user what to do in the incoming experiment
Has a settings button that allows the experiment operator to change file names and times
Has an "I'm ready" button to start
'''
class InfoWindow(QWidget):
    def __init__(self, scenario):
        super().__init__()
        
        layout = QGridLayout()

        instructions = QTextEdit()
        instructions.setHtml(
            '''
            <div style="text-align: center">
                <span style="background-color: yellow">Instructions</span> for <em>control</em> scenario: Press the <span style="font-weight: bold">Emergency</span> button when an <span style="text-decoration: underline">emergency</span> situation arises.
            </div>
            '''
        )
        instructions.setReadOnly(True)
        self.readyButton = QPushButton("Ready")
        
        if scenario != "C":
            instructions.setHtml(
            '''
            <div style="text-align: center">
                <span style="background-color: yellow">Instructions</span> for <em>trivial</em> scenario: Press the <span style="font-weight: bold">Do Task</span> button when <span style="text-decoration: underline">prompted</span>.
                Press the <span style="font-weight: bold">Emergency</span> button when an <span style="text-decoration: underline">emergency</span> situation arises.
            </div>
            '''
        )
        
        instructions.setObjectName("instructions")
        self.readyButton.setObjectName("readyButton")

        layout.addWidget(instructions, 1, 1, 1, 2)
        layout.addWidget(self.readyButton, 2, 1, 1, 2)
        layout.addWidget(QWidget(), 0, 3)
        layout.addWidget(QWidget(), 3, 0)

        self.setLayout(layout)

    def setReadyButton(self, parentFunc):
        self.readyButton.clicked.connect(parentFunc)