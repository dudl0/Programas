import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout

def greet():
    label.setText("Olá, Mundo!")

app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle("Hello World App")
window.resize(500,500)

layout = QVBoxLayout()

label = QLabel("")
layout.addWidget(label)

button = QPushButton("Clique aqui")
button.clicked.connect(greet)
layout.addWidget(button)

window.setLayout(layout)

window.show()

sys.exit(app.exec_())
