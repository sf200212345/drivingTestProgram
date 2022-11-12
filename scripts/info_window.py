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
            <div style="text-align: left">
                <p>In this study, we try to simulate the experience of driving an autonomous car. The autonomous system installed in the car in this study is capable of sensing its environment and operating without human involvement. In the case of an emergency, the autonomous car will give you a warning on the display screen. You will need to click on the red “Emergency” button below the video to resume the control of the car.</p>
                <p style="font-weight: bold">To simulate the driving experience, please keep your hand on the mouse the entire time during the simulation experience as if you were holding the steering wheel. Other than that, you do not need to perform any other tasks unless if an emergency occurs. Simply watch the screen as you drive through the countryside as if you were present in the car.</p>
                <p style="font-weight: bold">Please put your hand on the mouse now.</p>
            </div>
            '''
        )
        instructions.setReadOnly(True)
        self.readyButton = QPushButton("Ready")
        
        if scenario != "C":
            instructions.setHtml(
            '''
            <div style="text-align: left">
                <p>In this study, we try to simulate the experience of driving an autonomous car. The autonomous system installed in the car in this study is capable of sensing its environment and operating without human involvement. In the case of an emergency, the autonomous car will give you a warning on the display screen. You will need to click on the red “Emergency” button below the video to resume the control of the car.</p>
                <p style="font-weight: bold">To simulate the driving experience, please keep your hand on the mouse the entire time during the simulation experience as if you were holding the steering wheel. The company that makes the autonomous car has designed a system to engage drivers and make sure the drivers are not being distracted to avoid accidents, even though they are not actively operating the car. Therefore, you will see a green button appears throughout the video. Every time you see it, click on the “I am paying attention” button below the video.</p>
                <p style="font-weight: bold">Please put your hand on the mouse now.</p>
            </div>
            '''
        )
        
        instructions.setObjectName("instructions")
        self.readyButton.setObjectName("readyButton")

        layout.addWidget(instructions, 0, 1, 3, 2)
        layout.addWidget(self.readyButton, 2, 1, 2, 2)
        layout.addWidget(QWidget(), 0, 3)
        layout.addWidget(QWidget(), 3, 0)

        self.setLayout(layout)

    def setReadyButton(self, parentFunc):
        self.readyButton.clicked.connect(parentFunc)