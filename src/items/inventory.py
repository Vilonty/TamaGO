from src.items.food import Food
from src.items.pills import Pills
from src.items.drugs import Drug

from src.log.logger_config import  logger

class Inventory:

    def __init__(self, hunger, health, happy):

        self.items_food = Food
        self.items_pills = Pills
        self.items_drug = Drug

        self.hunger = hunger
        self.health = health
        self.happy = happy

    def show_inventory(self):

        logger.info("включение инвентаря")

        print("\nИнвентарь")

        all_items = (
            ("Еда", self.items_food.getfoodlist()),
            ("Таблетки", self.items_pills.getpillslist()),
            ("Наркотики", self.items_drug.getdrugslist())
        )


        alert_info = lambda item: print(f"{item['name']} id: {item['id']} : {item['col']} шт.")

        has_items = False

        for category_name, items_list in all_items:
            print(f"\n{category_name}:")
            category_has_items = False

            for item in items_list:
                if item['col'] > 0:
                    alert_info(item)
                    category_has_items = True
                    has_items = True

            if not category_has_items:
                print(f"{category_name} нет")

        if not has_items:
            print("\nИнвентарь пуст.")

        self.move = input("\nДля использования предмета введите его id (или 'b' для выхода): ")

        if self.move.lower() == "b":
            logger.info("выход из инвентаря")
            return

        try:
            item_id = int(self.move)
            self.use_items(item_id)

        except ValueError:
            logger.info("введение неправильного предмета")
            print("Введено неправильное значение")

    def get_items_by_category(self, category):
        """Получаем предметы по категории"""
        if category == "ЕДА":
            return self.items_food.getfoodlist()
        elif category == "ТАБЛЕТКИ":
            return self.items_pills.getpillslist()
        elif category == "НАРКОТИКИ":
            return self.items_drug.getdrugslist()
        return []

    def get_item_by_id(self, item_id):
        """Получаем предмет по ID"""
        full_items = (
                self.items_food.getfoodlist() +
                self.items_pills.getpillslist() +
                self.items_drug.getdrugslist()
        )

        for item in full_items:
            if item.get('id') == item_id:
                return item
        return None

    def use_items(self, item_id):
        logger.info(f"выбор предмета с id: {item_id}")

        # Находим предмет во всех категориях
        item = None
        category = None

        # Ищем предмет в соответствующих категориях
        if 1 <= item_id <= 99:
            category = self.items_food.getfoodlist()
        elif 100 <= item_id <= 199:
            category = self.items_pills.getpillslist()
        elif 200 <= item_id <= 299:
            category = self.items_drug.getdrugslist()

        if category:
            for it in category:
                if it['id'] == item_id:
                    item = it
                    break

        # Проверяем наличие предмета
        if not item or item['col'] <= 0:
            print("Предмет не найден или закончился")
            return False

        try:
            # Используем предмет и уменьшаем количество
            success = False
            if item['type'] == 'food':
                success = self.hunger.Eat(item['id'])
            elif item['type'] == 'pills':
                if self.health.healthst == 1:
                    print('Питомец здоров')
                    success = False
                else:
                    success = self.health.Regen(item['id'])
            elif item['type'] == 'drug':
                success = self.happy.overjoy(item['id'])

            # Если использование успешно - уменьшаем количество
            if success:
                item['col'] -= 1
                print(f"Использован {item['name']}. Осталось: {item['col']}")
                return True


            return True

        except Exception as e:
            print(f"Ошибка при использовании: {str(e)}")
            return False

