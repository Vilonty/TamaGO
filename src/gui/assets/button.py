from PyQt6.QtWidgets import QPushButton, QSizePolicy

class ExpandingButton(QPushButton):
    def __init__(self, text):
        super().__init__(text)
        btn = QPushButton(text)
        self.setSizePolicy(QSizePolicy.Policy.Preferred , QSizePolicy.Policy.Fixed)
