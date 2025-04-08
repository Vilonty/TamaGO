from PyQt6.QtWidgets import (QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
                             QLabel, QFrame, QPushButton, QMessageBox)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFontDatabase
from src.gui.utils.icon_menager import IconManager
import os
import platform
import subprocess


class Settings(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        QFontDatabase.addApplicationFont("fonts/PressStart2P-Regular.ttf")
        self.init_ui()
        self.load_styles()
        IconManager.set_window_icon(self)

    def init_ui(self):
        self.setWindowTitle("Тамагочи настройки")
        self.setWindowState(Qt.WindowState.WindowMaximized)

        central_widget = QWidget()
        central_widget.setObjectName("mainWidget")
        self.setCentralWidget(central_widget)

        main_layout = QHBoxLayout(central_widget)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)

        # Левая панель (для кнопки "О авторе")
        left_panel = QFrame()
        left_panel.setObjectName("leftPanel")
        left_layout = QVBoxLayout(left_panel)
        left_layout.setContentsMargins(0, 0, 0, 0)
        left_layout.setSpacing(0)

        back_btn = QPushButton("Вернуться")
        back_btn.setObjectName("backButton")
        back_btn.setFixedSize(200, 50)
        back_btn.clicked.connect(self.go_back)
        left_layout.addWidget(back_btn, alignment=Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignTop)

        # Пустое пространство сверху
        left_layout.addStretch()

        # Кнопка "О авторе" внизу слева
        about_btn = QPushButton("О авторе")
        about_btn.setObjectName("aboutButton")
        about_btn.setFixedSize(200, 50)
        about_btn.clicked.connect(self.show_about)
        left_layout.addWidget(about_btn, alignment=Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignBottom)

        # Центральный белый блок
        center_frame = QFrame()
        center_frame.setObjectName("settingsCenterFrame")
        center_frame.setFixedSize(600, 600)

        center_layout = QVBoxLayout(center_frame)
        center_layout.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignHCenter)
        center_layout.setContentsMargins(20, 20, 20, 20)
        center_layout.setSpacing(20)

        # Заголовок "НАСТРОЙКИ"
        title_label = QLabel("НАСТРОКИ")
        title_label.setObjectName("settingsTitle")
        title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        center_layout.addWidget(title_label)

        # Кнопка "ИЗМЕНИТЬ ФОН"
        change_bg_btn = QPushButton("ИЗМЕНИТЬ ФОН")
        change_bg_btn.setObjectName("settingsButton")
        change_bg_btn.setFixedSize(200, 50)
        change_bg_btn.clicked.connect(self.open_images_folder)
        center_layout.addWidget(change_bg_btn, alignment=Qt.AlignmentFlag.AlignCenter)

        # Правая панель (только с кнопкой "Информация")
        right_panel = QFrame()
        right_panel.setObjectName("rightPanel")
        right_layout = QVBoxLayout(right_panel)
        right_layout.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignRight)
        right_layout.setContentsMargins(0, 10, 10, 0)

        info_btn = QPushButton("Информация")
        info_btn.setObjectName("infoButton")
        info_btn.setFixedSize(170, 50)
        info_btn.clicked.connect(self.show_info)
        right_layout.addWidget(info_btn)

        # Добавляем все панели в главный layout
        main_layout.addWidget(left_panel, stretch=0)
        main_layout.addStretch(1)
        main_layout.addWidget(center_frame)
        main_layout.addStretch(1)
        main_layout.addWidget(right_panel, stretch=0)

    def open_images_folder(self):
        """Открывает папку images/main в проводнике системы"""
        base_dir = os.path.dirname(os.path.abspath(__file__))
        images_path = os.path.join(base_dir, "..", "images", "main")

        try:
            if platform.system() == "Windows":
                os.startfile(images_path)
            elif platform.system() == "Darwin":  # macOS
                subprocess.run(["open", images_path])
            else:  # Linux и другие Unix-системы
                subprocess.run(["xdg-open", images_path])
        except Exception as e:
            QMessageBox.warning(
                self,
                "Ошибка",
                f"Не удалось открыть папку с фонами:\n{str(e)}"
            )

    def show_info(self):
        text = (
            "Игра Тамагочи\n\n"
            "Чтобы начать игру нажмите 'Начать игру' и введите имя питомца.\n"
            "Ваша цель - поддерживать в нём жизнь. Если питомец умрёт - вы проиграете :("
        )
        msg = QMessageBox()
        msg.setWindowTitle("Информация")
        msg.setText(text)
        msg.exec()

    def show_about(self):
        msg = QMessageBox()
        msg.setWindowTitle("Об авторе")
        msg.setText("Vilonty")
        msg.exec()

    def go_back(self):

        self.close()

    def load_styles(self):
        base_dir = os.path.dirname(__file__)
        style_path = os.path.join(base_dir, "..", "gui", "style", "settings.qss")

        try:
            with open(style_path, "r", encoding="utf-8") as f:
                self.setStyleSheet(f.read())
        except Exception as e:
            print(f"Ошибка загрузки стилей: {str(e)}")