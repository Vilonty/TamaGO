# src/gui/utils/icon_manager.py
import os
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QApplication
from PyQt6.QtWidgets import QMainWindow


class IconManager:
    @staticmethod
    def set_app_icon(app: QApplication):
        """Устанавливает иконку для всего приложения"""
        base_dir = Path(__file__).parent.parent.parent
        icon_path = str(base_dir / "images" / "icon" / "tamagotchi_icon.ico")

        if os.path.exists(icon_path):
            app.setWindowIcon(QIcon(icon_path))
        else:
            print(f"Файл иконки не найден: {icon_path}")
    @staticmethod
    def set_window_icon(window: QMainWindow, icon_path: str = None):
        """
        Устанавливает иконку для окна

        :param window: Экземпляр QMainWindow
        :param icon_path: Путь к иконке (если None, используется путь по умолчанию)
        """
        if icon_path is None:
            base_dir = os.path.dirname(os.path.abspath(__file__))
            icon_path = os.path.join(base_dir, "..", "..", "images", "icons","icon.ico")

        if os.path.exists(icon_path):
            window.setWindowIcon(QIcon(icon_path))
        else:
            print(f"Файл иконки не найден: {icon_path}")