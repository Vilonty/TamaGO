import logging
import os

def setup_logger():

    log_file = os.path.join('log', 'tamagochi.log')

    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s\n',
        filename=log_file,
        filemode='a',
        encoding='utf-8'
    )

    return logging.getLogger(__name__)

logger = setup_logger()