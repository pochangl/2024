import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout

app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle('Simple PyQt App with QLabel')
window.setGeometry(0, 0, 640, 480)
label = QLabel('Hello, PyQt!')
layout = QVBoxLayout()
layout.addWidget(label)
window.setLayout(layout)
window.show()
sys.exit(app.exec())