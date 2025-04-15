# game_window.py (графический интерфейс)
import os
from PyQt6.QtWidgets import (QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
                             QLabel, QFrame, QPushButton)
from PyQt6.QtCore import Qt, QTimer, pyqtSignal
from PyQt6.QtGui import QPixmap
from src.mainprocesses.dead import DeadMenager
import time
from PyQt6.QtGui import QPixmap, QIcon
from PyQt6.QtWidgets import QMessageBox
from src.gui.utils.icon_menager import IconManager

class MainWindowGame(QMainWindow):
    gameClosed = pyqtSignal()

    def __init__(self, tamago):
        super().__init__()
        self.tamago = tamago
        self.start_time = time.time()
        self.total_duration = 600
        self.init_ui()
        self.load_styles()
        IconManager.set_window_icon(self)
        self.setup_game_timer()

    def init_ui(self):
        self.setWindowTitle("Tamagochi")
        self.setWindowState(Qt.WindowState.WindowMaximized)

        central_widget = QWidget()
        central_widget.setObjectName("mainWidget")
        self.setCentralWidget(central_widget)

        main_layout = QVBoxLayout(central_widget)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)

        # Верхняя полоса времени
        self.time_bar = QFrame()
        self.time_bar.setFixedHeight(30)
        self.time_bar.setObjectName("timeBar")
        self.time_progress = QFrame(self.time_bar)
        self.time_progress.setObjectName("timeProgress")
        main_layout.addWidget(self.time_bar)

        # Основной контент
        content_widget = QWidget()
        content_layout = QHBoxLayout(content_widget)
        content_layout.setContentsMargins(20, 30, 20, 20)
        main_layout.addWidget(content_widget)

        # Левая панель (картинка и таймер)
        left_panel = QWidget()
        left_layout = QVBoxLayout(left_panel)
        left_layout.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignLeft)

        # Картинка над таймером
        self.time_image = QLabel()
        self.time_image.setContentsMargins(20, 0, 0, 0)
        self.load_time_image()
        left_layout.addWidget(self.time_image, alignment=Qt.AlignmentFlag.AlignLeft)

        # Таймер
        self.timer_label = QLabel("10:00")
        self.timer_label.setObjectName("timerLabel")
        left_layout.addWidget(self.timer_label, alignment=Qt.AlignmentFlag.AlignLeft)

        content_layout.addWidget(left_panel)

        # Центральная панель
        center_panel = QWidget()
        center_layout = QVBoxLayout(center_panel)
        center_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        center_layout.setSpacing(5)

        self.name_label = QLabel(self.tamago.name)
        self.name_label.setObjectName("tamagoName")
        self.name_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        center_layout.addWidget(self.name_label)

        # Изображение тамагочи с белым фоном
        self.tama_container = QFrame()
        self.tama_container.setMinimumSize(200, 200)
        self.tama_container.setStyleSheet("background-color: white;")
        tama_layout = QVBoxLayout(self.tama_container)
        tama_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.tama_image = QLabel()
        self.tama_image.setFixedSize(300, 300)
        tama_layout.addWidget(self.tama_image)
        center_layout.addWidget(self.tama_container)

        # Полоски состояний с картинками
        self.setup_status_bars(center_layout)

        # Кнопка инвентаря (картинка)
        self.inv_btn = QPushButton()
        self.inv_btn.setObjectName("inventoryBtn")
        self.inv_btn.setFixedSize(70, 70)
        self.load_inventory_image()
        self.inv_btn.clicked.connect(self.open_inventory)
        center_layout.addWidget(self.inv_btn, alignment=Qt.AlignmentFlag.AlignCenter)

        content_layout.addWidget(center_panel, stretch=1)

        # Правая панель (кнопка вопроса)
        right_panel = QWidget()
        right_layout = QVBoxLayout(right_panel)
        right_layout.setAlignment(Qt.AlignmentFlag.AlignTop)

        # Кнопка вопроса
        self.question_btn = QPushButton("?")
        self.question_btn.setObjectName("questionBtn")
        self.question_btn.setFixedSize(50, 50)
        self.question_btn.clicked.connect(self.show_info)
        right_layout.addWidget(self.question_btn)
        self.update_time_bar_color()

        content_layout.addWidget(right_panel)

    def open_inventory(self):
        try:
            from src.gui.InventoryWindow import MainWindowInventory
            if not hasattr(self, 'inventory_window'):
                self.inventory_window = MainWindowInventory(self, self.tamago)  # Передаем и parent и tamago
            self.inventory_window.show()
        except Exception as e:
            print(f"Ошибка при открытии инвентаря: {str(e)}")
            import traceback
            traceback.print_exc()

    def update_time_bar_color(self):
        if hasattr(self.tamago, 'health') and self.tamago.health.healthst == 0:
            # Болотно-зеленый цвет при болезни
            self.time_progress.setStyleSheet("""
                background-color: #6b8e23;
                border: 2px solid #556b2f;
                border-radius: 8px;
            """)
        else:
            # Обычный голубой цвет
            self.time_progress.setStyleSheet("""
                background-color: #7fdbff;
                border: 2px solid #5dade2;
                border-radius: 8px;
            """)
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

    def load_time_image(self):
        base_dir = os.path.dirname(os.path.abspath(__file__))
        image_path = os.path.join(base_dir, "..", "images","game", "time.png")
        if os.path.exists(image_path):
            pixmap = QPixmap(image_path)
            self.time_image.setPixmap(pixmap.scaled(
                70, 70,
                Qt.AspectRatioMode.KeepAspectRatio,
                Qt.TransformationMode.SmoothTransformation
            ))

    def load_inventory_image(self):
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        image_path = os.path.join(base_dir, "images", "game", "inv.png")
        if os.path.exists(image_path):
            pixmap = QPixmap(image_path)
            # Создаем QIcon из QPixmap
            icon = QIcon(pixmap)
            self.inv_btn.setIcon(icon)
            self.inv_btn.setIconSize(pixmap.size())
        else:
            print(f"Файл не найден: {image_path}")

    def setup_status_bars(self, layout):
        stats = [
            ("Здоровье", "#e74c3c", self.tamago.health.healthlv, "zdr.png"),
            ("Голод", "#f1c40f", self.tamago.hunger.weight, "food.png"),
            ("Счастье", "#3498db", self.tamago.happy.happylv, "ch.png")
        ]

        for name, color, value, image in stats:
            container = QWidget()
            vbox = QVBoxLayout(container)
            vbox.setAlignment(Qt.AlignmentFlag.AlignCenter)
            vbox.setContentsMargins(0, 0, 0, 0)
            vbox.setSpacing(1)

            # Картинка статуса
            icon = QLabel()
            icon.setMinimumSize(45, 45)
            self.load_status_icon(icon, image)
            vbox.addWidget(icon, alignment=Qt.AlignmentFlag.AlignCenter)

            # Текст под картинкой
            value_label = QLabel(f"{value}/100")
            value_label.setObjectName("statusValue")
            vbox.addWidget(value_label, alignment=Qt.AlignmentFlag.AlignCenter)

            # Полоска состояния
            bar = QFrame()
            bar.setMinimumSize(300, 8)
            bar.setStyleSheet(f"""
                QFrame {{
                    background-color: {color};
                    border-radius: 7px;
                }}
            """)
            vbox.addWidget(bar)

            setattr(self, f"{name.lower()}_label", value_label)
            setattr(self, f"{name.lower()}_bar", bar)
            layout.addWidget(container)

    def load_status_icon(self, label, image_name):
        # Получаем абсолютный путь к директории src
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        image_path = os.path.join(base_dir, "images", "game",image_name)
        print(image_path)  # Должно выводить D:\проекты\мусор\TamagoMain\src\images\zdr.png и т.д.

        if os.path.exists(image_path):
            pixmap = QPixmap(image_path)
            label.setPixmap(pixmap.scaled(
                70, 70,
                Qt.AspectRatioMode.KeepAspectRatio,
                Qt.TransformationMode.SmoothTransformation
            ))
        else:
            print(f"Файл не найден: {image_path}")

    def setup_game_timer(self):
        self.game_timer = QTimer()
        self.game_timer.timeout.connect(self.game_loop)
        self.game_timer.start(1000)

    def game_loop(self):
        try:
            # Обновление времени
            current_time = time.time()
            elapsed = current_time - self.start_time
            remaining = max(0, self.total_duration - elapsed)

            # Обновление таймера
            mins, secs = divmod(int(remaining), 60)
            self.timer_label.setText(f"{mins:02d}:{secs:02d}")

            # Обновление полосы времени
            if self.time_bar.width() > 0:
                progress = remaining / self.total_duration
                self.time_progress.setFixedWidth(int(self.time_bar.width() * progress))

            # Обновление цвета полоски в зависимости от состояния здоровья
            self.update_time_bar_color()

            # Обновление состояний
            self.update_status_bars()
            self.update_image()

            # Проверка смерти
            if not DeadMenager.alive():
                self.game_timer.stop()
                self.close()
                self.gameClosed.emit()
        except Exception as e:
            print(f"Ошибка в игровом цикле: {str(e)}")

    def update_status_bars(self):
        # Обновляем значения и прогресс-бары
        health = max(0, min(100, self.tamago.health.healthlv))  # Ограничиваем 0-100
        self.здоровье_label.setText(f"{health}/100")
        self.здоровье_bar.setFixedWidth(int(300 * (health / 100)))  # Добавлена закрывающая скобка

        hunger = max(0, min(100, self.tamago.hunger.weight))  # Ограничиваем 0-100
        self.голод_label.setText(f"{hunger}/100")
        self.голод_bar.setFixedWidth(int(300 * (hunger / 100)))  # Добавлена закрывающая скобка

        happy = max(0, min(100, self.tamago.happy.happylv))  # Ограничиваем 0-100
        self.счастье_label.setText(f"{happy}/100")
        self.счастье_bar.setFixedWidth(int(300 * (happy / 100)))  # Добавлена закрывающая скобка

    def update_image(self):
        health = self.tamago.health.healthlv
        img = 1
        if health >= 75:
            img = 1
        elif health >= 50:
            img = 2
        elif health >= 30:
            img = 3
        elif health >= 10:
            img = 4
        else:
            img = 5

        base_dir = os.path.dirname(os.path.abspath(__file__))
        image_path = os.path.join(
            base_dir, "..", "images", "tamagoface", "main", f"{img}.png"
        )

        if os.path.exists(image_path):
            pixmap = QPixmap(image_path)
            self.tama_image.setPixmap(pixmap.scaled(
                300, 300,
                Qt.AspectRatioMode.KeepAspectRatio,
                Qt.TransformationMode.SmoothTransformation
            ))
        else:
            print(f"Изображение не найдено: {image_path}")

    def load_styles(self):
        base_dir = os.path.dirname(__file__)
        style_path = os.path.join(base_dir, "..", "gui", "style", "game_style.qss")

        try:
            with open(style_path, "r", encoding="utf-8") as f:
                self.setStyleSheet(f.read())
        except Exception as e:
            print(f"Ошибка загрузки стилей: {str(e)}")

    def closeEvent(self, event):
        self.gameClosed.emit()
        super().closeEvent(event)