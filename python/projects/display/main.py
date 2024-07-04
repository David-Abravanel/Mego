from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton


app = QApplication([])

win = QMainWindow()

button = QPushButton('My Button')
def calledBtn(a):
    print(a)
button.clicked.connect(calledBtn)

win.setCentralWidget(button)
win.show()

app.exec()