import sys
from PyQt5.QtWidgets import (
    QApplication,
    QDialog,
    QDialogButtonBox,
    QLabel,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
)
global textCustom, titleCustom
textCustom = titleCustom = ''
class CustomDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent=parent)

        self.setWindowTitle(titleCustom)

        QBtn = QDialogButtonBox.Ok | QDialogButtonBox.Cancel

        self.buttonBox = QDialogButtonBox(QBtn)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

        self.layout = QVBoxLayout()
        message = QLabel(textCustom)
        self.layout.addWidget(message)
        self.layout.addWidget(self.buttonBox)
        self.setLayout(self.layout)
        
class Alert_CustomDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent=parent)

        self.setWindowTitle(titleCustom)

        QBtn = QDialogButtonBox.Ok

        self.buttonBox = QDialogButtonBox(QBtn)
        self.buttonBox.accepted.connect(self.accept)
        # self.buttonBox.rejected.connect(self.reject)

        self.layout = QVBoxLayout()
        message = QLabel(textCustom)
        self.layout.addWidget(message)
        self.layout.addWidget(self.buttonBox)
        self.setLayout(self.layout)

# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()

#         # self.setWindowTitle("My App")

#         # button = QPushButton("Press me for a dialog!")
#         # button.clicked.connect(self.button_clicked)
#         # self.setCentralWidget(button)
#         self.button_clicked()
#     def button_clicked(self):
#         print("click")

#         dlg = CustomDialog()  # If you pass self, the dialog will be centered over the main window as before.
#         if dlg.exec_():
#             print("Success!")
#         else:
#             print("Cancel!")

# app = QApplication(sys.argv)

# window = MainWindow()
# window.show()

# app.exec_()