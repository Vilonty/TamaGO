import os
import sys
import subprocess
from PyQt6.QtWidgets import (QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
                             QLabel, QFrame, QPushButton, QInputDialog)
from PyQt6.QtCore import Qt, QTimer
from PyQt6.QtGui import QPixmap
from src.gui.assets.buttonFabric import fabricButton
from src.gui.utils.icon_menager import IconManager
from PyQt6.QtGui import QFontDatabase
from PyQt6.QtWidgets import QMessageBox


class MainWindow(QMainWindow):
    def __init__(self, app_manager):
        super().__init__()
        self.app_manager = app_manager
        self.current_image = 1
        self.init_ui()
        self.setup_animation()
        self.load_styles()
        IconManager.set_window_icon(self)

    def init_ui(self):
        self.setWindowTitle("Тамагочи")
        self.setWindowState(Qt.WindowState.WindowMaximized)

        central_widget = QWidget()
        central_widget.setObjectName("mainWidget")
        self.setCentralWidget(central_widget)

        main_layout = QHBoxLayout(central_widget)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)

        self.setup_left_panel(main_layout)
        self.setup_center_panel(main_layout)
        self.setup_right_panel(main_layout)

    def setup_left_panel(self, main_layout):
        left_panel = QFrame()
        left_panel.setObjectName("leftPanel")

        layout = QVBoxLayout(left_panel)
        layout.setSpacing(10)
        layout.setContentsMargins(0, 0, 0, 0)

        buttons = [
            ("defoult", "Начать игру", self.start_game),
            ("defoult", "Посмотреть логи", self.show_logs),
            ("defoult", "Предметы", self.items_show),
            ("defoult", "Настройки", self.settings),
            ("defoult", "Выход", self.close)
        ]

        for btn_type, text, handler in buttons:
            btn = fabricButton.create_button(btn_type, text)
            btn.clicked.connect(handler)
            layout.addWidget(btn)

        about_btn = fabricButton.create_button("defoult", "О авторе")
        about_btn.clicked.connect(self.show_about)  # Добавить эту строку
        layout.addStretch(1)
        layout.addWidget(about_btn, alignment=Qt.AlignmentFlag.AlignLeft)

        main_layout.addWidget(left_panel, stretch=0)

    def show_about(self):
        msg = QMessageBox()
        msg.setWindowTitle("Об авторе")
        msg.setText("Vilonty")
        msg.exec()

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

    def setup_center_panel(self, main_layout):
        center_panel = QFrame()
        center_panel.setObjectName("centerPanel")

        layout = QVBoxLayout(center_panel)
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.image_label = QLabel()
        self.image_label.setObjectName("tamaImage")
        self.image_label.setFixedSize(300, 300)
        layout.addWidget(self.image_label)

        main_layout.addWidget(center_panel, stretch=1)

    def setup_right_panel(self, main_layout):
        right_panel = QFrame()
        right_panel.setObjectName("rightPanel")

        layout = QVBoxLayout(right_panel)
        layout.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignRight)
        layout.setContentsMargins(0, 10, 10, 0)

        info_container = QWidget()
        info_layout = QHBoxLayout(info_container)
        info_layout.setContentsMargins(0, 0, 0, 0)

        info_btn = QPushButton("Информация")
        info_btn.setObjectName("infoButton")
        info_btn.setFixedSize(170, 50)
        info_btn.clicked.connect(self.show_info)


        info_layout.addWidget(info_btn)
        layout.addWidget(info_container)

        main_layout.addWidget(right_panel, stretch=0)

    def setup_animation(self):
        self.timer = QTimer()
        self.timer.timeout.connect(self.change_image)
        self.timer.start(3000)
        self.change_image()



    def show_logs(self):
        base_dir = os.path.dirname(os.path.abspath(__file__))
        # Исправленный путь: поднимаемся на 1 уровень вверх из папки gui
        log_path = os.path.join(base_dir, "..", "log", "tamagochi.log")

        try:
            # Создаем папку для логов если ее нет
            os.makedirs(os.path.dirname(log_path), exist_ok=True)

            if os.path.exists(log_path):
                if sys.platform == 'win32':
                    os.startfile(log_path)
                elif sys.platform == 'darwin':
                    subprocess.run(['open', log_path])
                else:
                    subprocess.run(['xdg-open', log_path])
            else:
                QMessageBox.warning(
                    self,
                    "Логи не найдены",
                    "Файл логов ещё не создан. Совершите первые действия в игре."
                )
        except Exception as e:
            QMessageBox.critical(
                self,
                "Ошибка",
                f"Не удалось открыть файл логов:\n{str(e)}"
            )



    def change_image(self):
        base_dir = os.path.dirname(os.path.abspath(__file__))
        image_path = os.path.join(base_dir, "..", "images", "tamagoface", "main", f"{self.current_image}.png")

        if os.path.exists(image_path):
            pixmap = QPixmap(image_path)
            self.image_label.setPixmap(pixmap.scaled(
                280, 280,
                Qt.AspectRatioMode.KeepAspectRatio,
                Qt.TransformationMode.SmoothTransformation
            ))
        else:
            self.image_label.setText(f"Image {self.current_image} not found")

        self.current_image = 1 if self.current_image >= 5 else self.current_image + 1

    def load_styles(self):
        base_dir = os.path.dirname(os.path.abspath(__file__))
        style_path = os.path.join(base_dir, "..", "gui", "style", "main_style.qss")

        try:
            with open(style_path, "r") as f:
                self.setStyleSheet(f.read())
        except Exception as e:
            print(f"Error loading styles: {str(e)}")

    def start_game(self):
        name, ok = QInputDialog.getText(
            self,
            'Создание питомца',
            'Введите имя вашего тамагочи:',
            text='Тамагоч'
        )
        if ok and name:
            self.app_manager.create_tamago(name)

    def items_show(self):
        from src.gui.ItemsShow import ItemsShow  # Импорт в методе, чтобы избежать циклических зависимостей
        self.items_window = ItemsShow(self)
        self.items_window.show()

    def settings(self):
        from src.gui.Settings import Settings
        self.items_window_setting = Settings(self)
        self.items_window_setting.show()



    def keyPressEvent(self, event):
        if event.key() == Qt.Key.Key_F11:
            self.toggle_fullscreen()
        super().keyPressEvent(event)

    def toggle_fullscreen(self):
        self.showFullScreen() if not self.isFullScreen() else self.showNormal()