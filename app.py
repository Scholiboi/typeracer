import sys
import time
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton


class TypingSpeedApp(QWidget):
    def __init__(self):
        super().__init__()
        self.result_label = None
        self.button = None
        self.label = None
        self.text_input = None
        self.build()
        self.start_time = None
        self.typing_active = False

    def build(self):
        layout = QVBoxLayout()

        self.label = QLabel("Click 'Start' and start typing below:", self)
        layout.addWidget(self.label)

        self.text_input = QLineEdit(self)
        layout.addWidget(self.text_input)

        self.button = QPushButton("Start", self)
        layout.addWidget(self.button)

        self.result_label = QLabel("", self)
        layout.addWidget(self.result_label)

        self.setLayout(layout)

        self.button.clicked.connect(self.start_or_stop)
        self.text_input.textChanged.connect(self.update_typing)

        self.setWindowTitle("Typing Speed Calculator")
        self.setGeometry(300, 300, 400, 200)

    def start_or_stop(self):
        if not self.typing_active:
            self.start_time = time.time()
            self.text_input.clear()
            self.text_input.setEnabled(True)
            self.typing_active = True
            self.button.setText("Stop")
            self.result_label.setText("")
        else:
            end_time = time.time()
            elapsed_time = end_time - self.start_time
            word_count = len(self.text_input.text().split())
            wpm = (word_count / elapsed_time) * 60 if elapsed_time > 0 else 0
            self.result_label.setText(f"Typing Speed: {wpm:.2f} WPM")
            self.typing_active = False
            self.button.setText("Start")
            self.text_input.setEnabled(False)

    def update_typing(self):
        if not self.typing_active:
            self.text_input.clear()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TypingSpeedApp()
    window.show()
    sys.exit(app.exec_())
