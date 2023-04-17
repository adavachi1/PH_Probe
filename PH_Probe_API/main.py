from datetime import datetime, timedelta
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget
from flask_sqlalchemy import SQLAlchemy
from PH import PH

app = QApplication(sys.argv)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('PH Values')

        widget = QWidget()
        layout = QVBoxLayout(widget)

        label = QLabel()
        layout.addWidget(label)

        self.setCentralWidget(widget)

        self.db = SQLAlchemy()
        self.db.init_app(app)
        self.db.app = app

        self.update_label()
        self.timer = app.createTimer(60000, self.update_label)
        self.timer.start()

    def update_label(self):
        start_time = datetime.utcnow() - timedelta(days=1)
        ph_values = self.db.session.query(PH).filter(PH.datetime >= start_time).all()

        text = ''
        for ph in ph_values:
            text += f'{ph.datetime}: {ph.value}\n'

        label = self.centralWidget().layout().itemAt(0).widget()
        label.setText(text)


if __name__ == '__main__':
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())