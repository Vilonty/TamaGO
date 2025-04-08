import sys
import os
from src.gui.MainGame import MainWindowGame
from PyQt6.QtWidgets import QApplication
from src.gui.MainWindow import MainWindow
from src.log.logger_config import logger
from PyQt6.QtWidgets import QMessageBox


class AppManager:
    def __init__(self):
        self.app = QApplication(sys.argv)
        self.main_window = MainWindow(self)
        self.tamago = None

    def run(self):
        self.main_window.show()
        sys.exit(self.app.exec())

    def create_tamago(self, name):
        try:
            if not name:
                raise ValueError("Имя не может быть пустым")

            from mainprocesses.tamago import Tamago
            self.tamago = Tamago(name)
            self.show_game_window()

        except Exception as e:
            QMessageBox.critical(
                self.main_window,
                "Ошибка",
                f"Не удалось создать питомца: {str(e)}"
            )

    def show_game_window(self):
        try:

            self.game_window = MainWindowGame(self.tamago)
            self.tamago.Live()
            self.main_window.hide()  # Скрываем вместо закрытия
            self.game_window.show()
        except Exception as e:
            print(f"Error: {str(e)}")
            import traceback
            traceback.print_exc()
            self.main_window.show()

if __name__ == '__main__':
    logger.info("Запуск приложения")
    manager = AppManager()
    manager.run()