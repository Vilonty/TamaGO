from src.items.food import Food
from src.items.pills import Pills
from src.items.drugs import Drug
from src.log.logger_config import logger

"""
тут фабричный метод для использования 
"""

class EdibleFactory:
    logger.info("запуск создания нужного экземпляра пищи")
    @staticmethod
    def create_edible(edible_type):
        if edible_type == "food":

            return Food()

        elif edible_type == "pills":

            return Pills()

        elif edible_type == "drug":

            return Drug()

        else:
            raise ValueError(f"Неизвестный тип съедобного объекта: {edible_type}")

        """сейчас 2 часа ночи мне вставать через 3, а я на середине кода и мне кажется скоро умру"""