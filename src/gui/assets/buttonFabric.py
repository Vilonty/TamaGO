from src.gui.assets.button import ExpandingButton
from PyQt6.QtWidgets import QPushButton

class fabricButton(QPushButton):
    @staticmethod
    def create_button(type_button, name):

        button = None

        if type_button == "defoult":
            button = ExpandingButton(name)

        return button