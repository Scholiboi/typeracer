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

        self.label = QLabel("Start typing below:", self)
        layout.addWidget(self.label)

        self.text_input = QLineEdit(self)
        layout.addWidget(self.text_input)

        self.button = QPushButton("Reset", self)
        layout.addWidget(self.button)

        self.result_label = QLabel("", self)
        layout.addWidget(self.result_label)

        self.setLayout(layout)

        self.button.clicked.connect(self.reset)
        self.text_input.textChanged.connect(self.start_or_update)
        self.text_input.returnPressed.connect(self.stop)

        self.setWindowTitle("Typing Speed Calculator")
        self.setGeometry(300, 300, 400, 200)

    def start_or_update(self):
        if not self.typing_active:
            self.start_time = time.time()
            self.typing_active = True
        else:
            intermediate_time = time.time()
            elapsed_time = intermediate_time - self.start_time
            word_count = len(self.text_input.text().split())
            wpm = (word_count / elapsed_time) * 60 if elapsed_time > 0 else 0
            self.result_label.setText(f"Current Typing Speed: {wpm:.2f} WPM")

    def reset(self):
        print("starting over")
        self.text_input.clear()
        self.result_label.setText("")
        self.button.setText("Reset")
        self.text_input.setEnabled(True)
        self.typing_active = False


    def stop(self):
        end_time = time.time()
        elapsed_time = end_time - self.start_time
        word_count = len(self.text_input.text().split())
        wpm = (word_count / elapsed_time) * 60 if elapsed_time > 0 else 0
        self.result_label.setText(f"Final Typing Speed: {wpm:.2f} WPM")
        self.typing_active = False
        self.text_input.setEnabled(False) # disable the text input field


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TypingSpeedApp()
    window.show()
    sys.exit(app.exec_())
