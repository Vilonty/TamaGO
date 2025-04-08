import os.path
from PyQt6.QtWidgets import (QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
                             QLabel, QApplication, QFrame, QPushButton,
                             QScrollArea, QSizePolicy, QMessageBox)
from PyQt6.QtCore import Qt, QTimer
import sys
from PyQt6.QtGui import QPixmap, QIcon

from src.items.food import Food
from src.items.pills import Pills
from src.items.drugs import Drug
from src.gui.utils.icon_menager import IconManager


class ItemsShow(QMainWindow):
    def __init__(self, parent=None, tamago=None):
        super().__init__(parent)
        self.tamago = tamago
        # Инициализируем классы предметов
        self.food = Food()
        self.pills = Pills()
        self.drug = Drug()
        self.setWindowTitle("Каталог предметов")
        self.setWindowModality(Qt.WindowModality.NonModal)
        self.setWindowFlags(self.windowFlags() | Qt.WindowType.WindowStaysOnTopHint)
        self.resize(800, 600)
        self.init_ui()
        IconManager.set_window_icon(self)
        self.load_style()

    def init_ui(self):
        central_widget = QWidget()
        central_widget.setObjectName("itemsCatalogWidget")
        self.setCentralWidget(central_widget)

        main_layout = QVBoxLayout(central_widget)
        main_layout.setContentsMargins(10, 10, 10, 10)
        main_layout.setSpacing(10)

        # Заголовок
        title = QLabel("ВСЕ ПРЕДМЕТЫ В ИГРЕ")
        title.setObjectName("catalogTitle")
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        main_layout.addWidget(title)

        # Область с прокруткой
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_content = QWidget()
        scroll_layout = QVBoxLayout(scroll_content)
        scroll_layout.setAlignment(Qt.AlignmentFlag.AlignTop)

        # Получаем все предметы из инициализированных классов
        categories = {
            "ЕДА": self.food.getfoodlist(),
            "ТАБЛЕТКИ": self.pills.getpillslist(),
            "НАРКОТИКИ": self.drug.getdrugslist()
        }

        for category_name, items in categories.items():
            if not items:
                continue

            # Контейнер для категории
            category_frame = QFrame()
            category_frame.setObjectName("categoryFrame")
            category_layout = QVBoxLayout(category_frame)

            # Заголовок категории
            category_label = QLabel(category_name)
            category_label.setObjectName("categoryLabel")
            category_layout.addWidget(category_label)

            # Горизонтальная прокрутка для предметов
            items_scroll = QScrollArea()
            items_scroll.setWidgetResizable(True)
            items_scroll.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)

            items_container = QWidget()
            items_container_layout = QHBoxLayout(items_container)
            items_container_layout.setContentsMargins(0, 0, 0, 0)
            items_container_layout.setSpacing(15)

            for item in items:
                item_card = self.create_item_card(item)
                items_container_layout.addWidget(item_card)

            items_scroll.setWidget(items_container)
            category_layout.addWidget(items_scroll)
            scroll_layout.addWidget(category_frame)

        scroll_area.setWidget(scroll_content)
        main_layout.addWidget(scroll_area)

        # Кнопка закрытия
        close_btn = QPushButton("ЗАКРЫТЬ")
        close_btn.setObjectName("closeButton")
        close_btn.clicked.connect(self.close)
        main_layout.addWidget(close_btn, alignment=Qt.AlignmentFlag.AlignRight)
    def create_item_card(self, item):
        card = QFrame()
        card.setObjectName("itemCard")
        card.setFixedSize(150, 180)
        card.setCursor(Qt.CursorShape.PointingHandCursor)

        layout = QVBoxLayout(card)
        layout.setContentsMargins(5, 5, 5, 5)
        layout.setSpacing(5)
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Изображение предмета
        img = QLabel()
        img.setObjectName("itemImage")
        img.setFixedSize(100, 100)
        img.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.load_item_image(img, item)
        layout.addWidget(img)

        # Название предмета
        name_label = QLabel(item['name'])
        name_label.setObjectName("itemName")
        name_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        name_label.setWordWrap(True)
        layout.addWidget(name_label)

        return card

    def load_item_image(self, label, item):
        """Загружает изображение предмета с правильными пропорциями"""
        try:
            # Получаем имя файла изображения из данных предмета
            image_name = item.get('img', 'default.png')
            base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

            # Пробуем несколько возможных путей
            possible_paths = [
                os.path.join(base_dir, "images", "game", image_name),
                os.path.join(base_dir, "images", "items", image_name),
                os.path.join(base_dir, "resources", "images", image_name)
            ]

            pixmap = None
            for path in possible_paths:
                if os.path.exists(path):
                    pixmap = QPixmap(path)
                    break

            if pixmap and not pixmap.isNull():
                # Сохраняем пропорции изображения
                label.setPixmap(pixmap.scaled(
                    label.width(), label.height(),
                    Qt.AspectRatioMode.KeepAspectRatio,
                    Qt.TransformationMode.SmoothTransformation
                ))
            else:
                label.setText("No Image")
                print(f"Image not found for item: {item['name']}")
        except Exception as e:
            print(f"Error loading image: {str(e)}")
            label.setText("Error")

    def load_style(self):
        base_dir = os.path.dirname(os.path.abspath(__file__))
        style_path = os.path.join(base_dir, "..", "gui", "style", "catalog_style.qss")

        try:
            with open(style_path, "r", encoding="utf-8") as f:
                self.setStyleSheet(f.read())
        except Exception as e:
            print(f"Error loading styles: {str(e)}")