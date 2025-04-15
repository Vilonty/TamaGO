import os.path
from PyQt6.QtWidgets import (QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
                             QLabel, QApplication, QFrame, QPushButton,
                             QScrollArea, QSizePolicy, QMessageBox)
from PyQt6.QtCore import Qt, QTimer
import sys
from PyQt6.QtGui import QPixmap, QIcon
from src.gui.utils.icon_menager import IconManager

class MainWindowInventory(QMainWindow):
    def __init__(self, parent=None, tamago=None):
        super().__init__(parent)
        self.tamago = tamago
        self.setWindowModality(Qt.WindowModality.NonModal)
        self.setWindowFlags(self.windowFlags() | Qt.WindowType.WindowStaysOnTopHint)
        self.init_ui()
        self.load_style()
        IconManager.set_window_icon(self)


    def closeEvent(self, event):
        if hasattr(self, 'update_timer'):
            self.update_timer.stop()
        super().closeEvent(event)

    def init_ui(self):
        self.setWindowTitle("Тамагочи - Инвентарь")
        self.setWindowState(Qt.WindowState.WindowMaximized)

        # Главный контейнер
        central_widget = QWidget()
        central_widget.setObjectName("mainWidget")
        self.setCentralWidget(central_widget)

        # Основной вертикальный макет
        main_layout = QVBoxLayout(central_widget)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)


        # Основной контент под линией
        content_widget = QWidget()
        content_layout = QHBoxLayout(content_widget)
        content_layout.setContentsMargins(20, 20, 20, 20)
        content_layout.setSpacing(20)


        # Левая панель (3 предмета)
        left_panel = self.create_left_panel()
        content_layout.addWidget(left_panel)

        for widget in self.findChildren(QFrame):
            if widget.objectName() == "topLine":
                widget.deleteLater()

        # Центральный инвентарь

        inventory_panel = self.create_inventory_panel()
        content_layout.addWidget(inventory_panel, stretch=1)

        # Правая панель (кнопка)
        right_panel = self.create_right_panel()
        content_layout.addWidget(right_panel)

        main_layout.addWidget(content_widget)
        self.show()

    def create_left_panel(self):
        panel = QFrame()
        panel.setObjectName("leftPanel")
        layout = QVBoxLayout(panel)
        layout.setSpacing(15)
        layout.setAlignment(Qt.AlignmentFlag.AlignTop)


        # Статусы (с проверкой на наличие tamago)
        stats = [
            ("Здоровье", "zdr.png"),
            ("Голод", "food.png"),
            ("Счастье", "ch.png")
        ]

        self.status_labels = {}

        for name, image in stats:
            container = QWidget()
            vbox = QVBoxLayout(container)
            vbox.setAlignment(Qt.AlignmentFlag.AlignCenter)
            vbox.setContentsMargins(0, 5, 0, 5)

            # Картинка статуса
            icon = QLabel()
            icon.setFixedSize(70, 70)
            self.load_status_icon(icon, image)
            vbox.addWidget(icon, alignment=Qt.AlignmentFlag.AlignCenter)

            # Текст под картинкой
            value = 100  # Значение по умолчанию
            if self.tamago:
                if name == "Здоровье":
                    value = self.tamago.health.healthlv
                elif name == "Голод":
                    value = self.tamago.hunger.weight
                elif name == "Счастье":
                    value = self.tamago.happy.happylv

            value_label = QLabel(f"{value}/100")
            value_label.setObjectName("statusValue")
            vbox.addWidget(value_label, alignment=Qt.AlignmentFlag.AlignCenter)

            self.status_labels[name.lower()] = value_label
            layout.addWidget(container)



        # Распорка чтобы прижать кнопку "Назад" к низу
        spacer = QWidget()
        spacer.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        layout.addWidget(spacer)

        # Кнопка "Назад"
        back_btn = QPushButton("НАЗАД")
        back_btn.setObjectName("backBtn")
        back_btn.setFixedHeight(40)
        back_btn.clicked.connect(self.close)
        layout.addWidget(back_btn, alignment=Qt.AlignmentFlag.AlignBottom)

        return panel

    def update_status_values(self):
        if hasattr(self, 'status_labels') and self.tamago:
            self.status_labels['здоровье'].setText(f"{self.tamago.health.healthlv}/100")
            self.status_labels['голод'].setText(f"{self.tamago.hunger.weight}/100")
            self.status_labels['счастье'].setText(f"{self.tamago.happy.happylv}/100")

    def load_time_image(self):
        base_dir = os.path.dirname(os.path.abspath(__file__))
        image_path = os.path.join(base_dir, "..", "images", "game", "time.png")
        if os.path.exists(image_path):
            pixmap = QPixmap(image_path)
            self.time_image.setPixmap(pixmap.scaled(
                70, 70,
                Qt.AspectRatioMode.KeepAspectRatio,
                Qt.TransformationMode.SmoothTransformation
            ))

    def load_status_icon(self, label, image_name):
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        image_path = os.path.join(base_dir, "images", "game", image_name)
        if os.path.exists(image_path):
            pixmap = QPixmap(image_path)
            label.setPixmap(pixmap.scaled(
                70, 70,
                Qt.AspectRatioMode.KeepAspectRatio,
                Qt.TransformationMode.SmoothTransformation
            ))
        else:
            print(f"Файл не найден: {image_path}")

    def create_inventory_panel(self):
        panel = QFrame()
        panel.setObjectName("inventoryPanel")
        main_layout = QVBoxLayout(panel)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)

        # Основная область с прокруткой
        scroll_area = QScrollArea()
        scroll_area.setObjectName("inventoryScrollArea")
        scroll_area.setWidgetResizable(True)
        scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)

        # Контент внутри ScrollArea
        content_widget = QWidget()
        content_layout = QVBoxLayout(content_widget)
        content_layout.setContentsMargins(15, 15, 15, 15)
        content_layout.setSpacing(25)

        # Заголовок инвентаря
        title = QLabel("ИНВЕНТАРЬ")
        title.setObjectName("inventoryTitle")
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        content_layout.addWidget(title)

        # Проверяем наличие инвентаря
        if not hasattr(self.tamago, 'inventory'):
            no_items_label = QLabel("Инвентарь недоступен")
            no_items_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
            content_layout.addWidget(no_items_label)
            scroll_area.setWidget(content_widget)
            main_layout.addWidget(scroll_area)
            return panel

        # Получаем категории из инвентаря
        categories = {
            "ЕДА": self.tamago.inventory.items_food.getfoodlist(),
            "ТАБЛЕТКИ": self.tamago.inventory.items_pills.getpillslist(),
            "НАРКОТИКИ": self.tamago.inventory.items_drug.getdrugslist()
        }

        for category_name, items in categories.items():
            # Пропускаем пустые категории
            if not items:
                continue

            # Контейнер для категории
            category_widget = QWidget()
            category_layout = QVBoxLayout(category_widget)
            category_layout.setSpacing(10)

            # Заголовок категории
            category_label = QLabel(category_name)
            category_label.setObjectName("categoryLabel")
            category_layout.addWidget(category_label)

            # Горизонтальная прокрутка для карточек
            cards_scroll = QScrollArea()
            cards_scroll.setWidgetResizable(True)
            cards_scroll.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)

            # Контейнер карточек
            cards_container = QWidget()
            cards_layout = QHBoxLayout(cards_container)
            cards_layout.setSpacing(15)
            cards_layout.setContentsMargins(0, 0, 0, 0)

            # Добавляем только те предметы, которые есть в инвентаре (col > 0)
            for item in items:
                if item['col'] > 0:
                    card = self.create_item_card(category_name, item)
                    cards_layout.addWidget(card)

            # Если в категории нет предметов, добавляем заглушку
            if cards_layout.count() == 0:
                no_items_label = QLabel(f"В категории {category_name} нет предметов")
                no_items_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
                cards_layout.addWidget(no_items_label)

            # Распорка для выравнивания влево
            spacer = QWidget()
            spacer.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
            cards_layout.addWidget(spacer)

            cards_scroll.setWidget(cards_container)
            category_layout.addWidget(cards_scroll)
            content_layout.addWidget(category_widget)

        scroll_area.setWidget(content_widget)
        main_layout.addWidget(scroll_area)

        return panel

    def create_item_card(self, category, item):
        card = QFrame()
        card.setObjectName("itemCard")
        card.setMinimumSize(100, 140)
        card.setMaximumSize(150, 200)
        card.setCursor(Qt.CursorShape.PointingHandCursor)

        layout = QVBoxLayout(card)
        layout.setContentsMargins(2, 2, 2, 2)  # Уменьшаем отступы
        layout.setSpacing(5)
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)  # Центрируем содержимое

        # Изображение
        img = QLabel()
        img.setObjectName("itemImage")  # Устанавливаем objectName для стилизации
        img.setFixedSize(75, 66)
        img.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.load_item_image(img, item)
        layout.addWidget(img, alignment=Qt.AlignmentFlag.AlignCenter)  # Явное центрирование

        # Текст
        text = QLabel()
        text.setObjectName("itemText")
        text.setAlignment(Qt.AlignmentFlag.AlignCenter)
        text.setWordWrap(True)

        item_text = f"{item['name']}\nКол-во: {item['col']}"
        if 'points' in item:
            item_text += f"\nЭффект: {item['points']}"

        text.setText(item_text)
        layout.addWidget(text)

        # Обработчик клика
        card.mousePressEvent = lambda event, cat=category, it=item: self.on_item_click(cat, it)

        return card

    def load_item_image(self, label, item):
        """Загружает изображение предмета на основе поля img в данных предмета"""
        try:
            # Базовый путь к папке с изображениями
            base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
            image_path = os.path.join(base_dir, "images", "game", item['img'])

            if os.path.exists(image_path):
                pixmap = QPixmap(image_path)
                label.setPixmap(pixmap.scaled(
                    75, 66,
                    Qt.AspectRatioMode.KeepAspectRatio,
                    Qt.TransformationMode.SmoothTransformation
                ))
            else:
                label.setText("No Image")
                print(f"Изображение не найдено: {image_path}")
        except Exception as e:
            print(f"Ошибка загрузки изображения: {str(e)}")
            label.setText("Error")

    def get_item_info(self, category, item_name):
        """Получаем информацию о предмете из логического инвентаря"""
        if not self.tamago or not hasattr(self.tamago, 'inventory'):
            return {"name": item_name, "count": 0, "effects": {}}

        # Преобразуем название для поиска
        item_id = self.get_item_id(category, item_name)

        if category == "ЕДА":
            items = self.tamago.inventory.items_food.getfoodlist()
        elif category == "ТАБЛЕТКИ":
            items = self.tamago.inventory.items_pills.getpillslist()
        else:
            items = self.tamago.inventory.items_drug.getdrugslist()

        for item in items:
            if item['id'] == item_id:
                return {
                    "name": item['name'],
                    "count": item['col'],
                    "effects": item.get('effects', {})
                }

        return {"name": item_name, "count": 0, "effects": {}}

    def get_item_id(self, category, item_name):
        """Сопоставляем имя предмета с его ID"""
        # Получаем список предметов для категории
        if category == "ЕДА":
            items = self.tamago.inventory.items_food.getfoodlist()
        elif category == "ТАБЛЕТКИ":
            items = self.tamago.inventory.items_pills.getpillslist()
        elif category == "НАРКОТИКИ":
            items = self.tamago.inventory.items_drug.getdrugslist()
        else:
            return 0

        # Ищем предмет по имени
        for item in items:
            if item['name'] == item_name:
                return item['id']

        return 0

    def format_item_info(self, item_info):
        """Форматируем информацию о предмете для отображения"""
        text = f"{item_info['name']}\n"

        if item_info['count'] > 0:
            text += f"Кол-во: {item_info['count']}\n"

            effects = item_info.get('effects', {})
            if 'health' in effects:
                text += f"ЗД: {effects['health']} "
            if 'hunger' in effects:
                text += f"ГОЛ: {effects['hunger']} "
            if 'happy' in effects:
                text += f"СЧ: {effects['happy']}"
        else:
            text += "Нет в инвентаре"

        return text

    def on_item_click(self, category, item):
        """Обработчик клика по предмету"""
        if not self.tamago or not hasattr(self.tamago, 'inventory'):
            QMessageBox.warning(self, "Ошибка", "Инвентарь недоступен")
            return

        try:
            # Проверяем, есть ли предмет в инвентаре
            if item['col'] <= 0:
                QMessageBox.warning(self, "Ошибка", "Этот предмет закончился")
                return

            # Используем предмет по его ID
            success = self.tamago.inventory.use_items(item['id'])

            if success:
                QMessageBox.information(self, "Успех", f"Вы использовали {item['name']}")

                self.update_inventory_display()
                self.update_status_values()
            else:
                QMessageBox.warning(self, "Ошибка", "Не удалось использовать предмет. Проверьте логику использования.")
        except Exception as e:
            QMessageBox.critical(self, "Ошибка", f"Произошла ошибка: {str(e)}")
            print(f"Ошибка при использовании предмета: {str(e)}")

    def update_inventory_display(self):
        """Обновляем отображение инвентаря"""
        # Находим область прокрутки инвентаря
        scroll_area = self.findChild(QScrollArea, "inventoryScrollArea")
        if not scroll_area:
            return

        # Получаем контент внутри ScrollArea
        content_widget = scroll_area.widget()
        if not content_widget:
            return

        # Обновляем все карточки предметов
        for category_widget in content_widget.findChildren(QWidget):
            for card in category_widget.findChildren(QFrame, "itemCard"):
                # Находим текстовый лейбл в карточке
                text_label = card.findChild(QLabel, "itemText")
                if text_label:
                    # Получаем текущий текст (название предмета)
                    current_text = text_label.text().split('\n')[0]

                    # Ищем предмет в инвентаре
                    item = self.find_item_by_name(current_text)
                    if item:
                        # Обновляем текст с новым количеством
                        new_text = f"{item['name']}\nКол-во: {item['col']}"
                        if 'points' in item:
                            new_text += f"\nЭффект: {item['points']}"
                        text_label.setText(new_text)

    def find_item_by_name(self, item_name):
        """Находит предмет в инвентаре по имени"""
        if not hasattr(self.tamago, 'inventory'):
            return None

        # Проверяем все категории
        categories = {
            "food": self.tamago.inventory.items_food.getfoodlist(),
            "pills": self.tamago.inventory.items_pills.getpillslist(),
            "drug": self.tamago.inventory.items_drug.getdrugslist()
        }

        for category_items in categories.values():
            for item in category_items:
                if item['name'] == item_name:
                    return item
        return None

    def create_right_panel(self):
        panel = QFrame()
        panel.setObjectName("rightPanel")
        layout = QVBoxLayout(panel)
        layout.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignRight)

        btn = QPushButton("?")
        btn.clicked.connect(self.show_info)
        btn.setObjectName("questionBtn")
        btn.setFixedSize(35, 35)
        layout.addWidget(btn)

        return panel

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
    """
    def create_left_panel(self):
        panel = QFrame()
        panel.setObjectName("leftPanel")
        layout = QVBoxLayout(panel)
        layout.setSpacing(15)
        layout.setAlignment(Qt.AlignmentFlag.AlignTop)

        # Предметы
        for _ in range(3):
            item_frame = QFrame()
            item_frame.setFixedSize(100, 120)
            item_layout = QVBoxLayout(item_frame)
            item_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

            img = QLabel()
            img.setFixedSize(80, 80)
            img.setStyleSheet("background: white; border: 1px solid gray;")

            text = QLabel("10/10")
            text.setObjectName("itemCaption")
            text.setAlignment(Qt.AlignmentFlag.AlignCenter)

            item_layout.addWidget(img)
            item_layout.addWidget(text)
            layout.addWidget(item_frame)

        # Распорка чтобы прижать кнопку к низу
        spacer = QWidget()
        spacer.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        layout.addWidget(spacer)

        # Кнопка Назад
        back_btn = QPushButton("НАЗАД")
        back_btn.setObjectName("backBtn")
        back_btn.setFixedHeight(40)
        back_btn.clicked.connect(self.close)
        layout.addWidget(back_btn)

        return panel
        """

    def load_style(self):
        base_dir = os.path.dirname(__file__)
        style_path = os.path.join(base_dir, "..", "gui", "style", "inventory_style.qss")

        try:
            with open(style_path, "r", encoding="utf-8") as f:
                self.setStyleSheet(f.read())
        except Exception as e:
            print(f"Ошибка загрузки стилей: {str(e)}")


