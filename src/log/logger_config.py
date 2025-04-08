import logging
import os


def setup_logger():
    log_file = os.path.join('log', 'tamagochi.log')

    # Убедитесь, что папка существует
    os.makedirs(os.path.dirname(log_file), exist_ok=True)

    # Явно укажите обработчик с UTF-8
    file_handler = logging.FileHandler(log_file, mode='a', encoding='utf-8')
    file_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))

    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    logger.addHandler(file_handler)

    return logger

logger = setup_logger()