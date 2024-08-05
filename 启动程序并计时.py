import sys
import time
import os
import subprocess
from flask import Flask, request
from PySide6.QtWidgets import (QApplication, QWidget, QVBoxLayout, QLabel,
                               QPushButton, QFileDialog, QLineEdit)
from PySide6.QtCore import Qt, QTimer
from threading import Thread

# 记住上次启动的程序路径的文件
last_program_file = 'last_program.txt'

# 加载上次启动的程序路径
def load_last_program():
    if os.path.exists(last_program_file):
        with open(last_program_file, 'r') as file:
            return file.read().strip()
    return ""

# 保存上次启动的程序路径
def save_last_program(program_path):
    with open(last_program_file, 'w') as file:
        file.write(program_path)

class TimerApp(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()
        self.timer_running = False
        self.start_time = None

    def initUI(self):
        layout = QVBoxLayout()

        self.timer_label = QLabel('00:00:000', self)
        self.timer_label.setAlignment(Qt.AlignCenter)
        self.timer_label.setStyleSheet("font-size: 20px;")
        layout.addWidget(self.timer_label)

        self.program_input = QLineEdit(load_last_program(), self)
        layout.addWidget(self.program_input)

        browse_button = QPushButton('选择程序', self)
        browse_button.clicked.connect(self.browse_program)
        layout.addWidget(browse_button)

        start_button = QPushButton('启动程序', self)
        start_button.clicked.connect(self.start_program)
        layout.addWidget(start_button)

        # stop_button = QPushButton('停止计时器', self)
        # stop_button.clicked.connect(self.stop_timer)
        # layout.addWidget(stop_button)

        self.setLayout(layout)
        self.setWindowTitle('计时器')
        self.setGeometry(300, 300, 400, 200)
        self.setWindowFlag(Qt.WindowStaysOnTopHint)

    def stop_timer(self):
        if self.timer_running:
            self.timer.stop()  # Stop the QTimer
            self.timer_running = False

    def browse_program(self):
        program_path, _ = QFileDialog.getOpenFileName(self, '选择程序', os.getenv('HOME'))
        if program_path:
            self.program_input.setText(program_path)

    def start_program(self):
        program_path = self.program_input.text()
        if program_path:
            save_last_program(program_path)
            subprocess.Popen(program_path)
            if not self.timer_running:
                self.start_timer()

    def start_timer(self):
        self.start_time = time.time()
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_timer)
        self.timer.start(10)  # 每10毫秒更新一次
        self.timer_running = True

    def update_timer(self):
        elapsed_time = time.time() - self.start_time
        milliseconds = int((elapsed_time - int(elapsed_time)) * 1000)
        minutes, seconds = divmod(int(elapsed_time), 60)
        self.timer_label.setText(f'{minutes:02d}:{seconds:02d}:{milliseconds:03d}')

    def stop_timer_from_request(self):
        self.stop_timer()

def create_flask_app(timer_app_instance):
    app = Flask(__name__)

    @app.route('/stop_timer', methods=['POST'])
    def stop_timer():
        timer_app_instance.stop_timer_from_request()
        print("Timer stopped from Flask request")
        return "Timer stopped", 200

    return app

def main():
    app = QApplication(sys.argv)
    timer_app = TimerApp()

    flask_app = create_flask_app(timer_app)
    flask_thread = Thread(target=flask_app.run, kwargs={'host': '0.0.0.0', 'port': 5000})
    flask_thread.daemon = True
    flask_thread.start()

    timer_app.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()
