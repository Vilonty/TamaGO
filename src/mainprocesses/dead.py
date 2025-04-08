"""
Статичный класс смерти

Используется во всей программе и заканчивает игру при функции kill

Он обрубает главный процесс, а так как все параллельные процессы - это процессы демоны, то игра заканчивается
"""
from src.log.logger_config import  logger

# src/mainprocesses/dead.py
class DeadMenager:
    livest = 1

    @staticmethod
    def kill():
        DeadMenager.livest = 0  # Убираем exit()

    @staticmethod
    def alive():
        logger.info("Запуск главных процессов")
        return DeadMenager.livest