from mainprocesses.tamago import Tamago
from mainprocesses.dead import DeadMenager
from src.log.logger_config import  logger




#Место откуда в консоль всё выводится
class UI:

    def __init__(self):

        logger.info("запуск UI")
        #Получение имени и экземпляра класса тамагойчи
        self.name = input('введите имя: ')
        self.tamago = Tamago(self.name)
        logger.info(f"Создан тамагочи с именем {self.name}")
        #Запуск функции дисплея
        self.Display()

    def Display(self):

        #Вывод имени питомца
        print('\nИмя питомца: ', self.name)

        #Старт жизни и запуск функционала игры
        self.tamago.Live()
        logger.info("Запуск жизни")
        self.Game()

    def Game(self):
        logger.info("Запуск игры")
        #Deadmenager это проверка смерти, пока тамагочи жив игра работает
        while DeadMenager.alive():

            #Основная консолька
            self.move = input("\nВведите действие: "
                              "\nУзнать информацию [1], "
                              "\nИнвентарь [2], "
                              "\nЗакончить игру [ext] ").lower()
            logger.info(f"Выбрано действие: {self.move}")
            #Действие 1
            if self.move == "1":

                print("\nВозраст: ", self.tamago.age,
                      " \nЗдоровье: ", self.tamago.health.healthlv,
                      " \nВес: ", self.tamago.hunger.weight,
                      " \nОжирение: ", self.tamago.hunger.obestylv,
                      " \nРадость: ", self.tamago.happy.happylv,
                      f" \nБолезнь: {'да' if self.tamago.health.healthst == 0 else 'нет'}")

            elif self.move == "2":
                logger.info("запуск инвентаря")
                self.tamago.inventory.show_inventory()

            #Выход из программы
            elif self.move == "ext":
                logger.info("выход из игры")
                self.tamago.Dead()

            #Минимальная обработка исключений в случае неправильно введёной команды
            else:
                logger.info("была выбрана неправильная команда")
                print("\nКоманда введена неверно")

#Запуск программы если файл называется main
if __name__ == '__main__':
    logger.info("инициализация программы")
    UI()
