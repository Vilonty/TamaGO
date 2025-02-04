from mainprocesses.tamago import Tamago
from mainprocesses.dead import DeadMenager

'''
ЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫ
Перегрузка операторов в over/over.py
ЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫ
'''




#Место откуда в консоль всё выводится
class UI:

    def __init__(self):

        #Получение имени и экземпляра класса тамагойчи
        self.name = input('введите имя: ')
        self.tamago = Tamago(self.name)

        #Запуск функции дисплея
        self.Display()

    def Display(self):

        #Вывод имени питомца
        print('\nИмя питомца: ', self.name)

        #Старт жизни и запуск функционала игры
        self.tamago.Live()
        self.Game()

    def Game(self):

        #Deadmenager это проверка смерти, пока тамагочи жив игра работает
        while DeadMenager.alive():

            #Основная консолька
            self.move = input("\nВведите действие: "
                              "\nУзнать информацию [1], "
                              "\nПокормить [2], "
                              "\nВылечить [3], "
                              "\nЗакончить игру [ext] ").lower()

            #Действие 1
            if self.move == "1":

                print("\nВозраст: ", self.tamago.age,
                      " \nЗдоровье: ", self.tamago.health.healthlv,
                      " \nВес: ", self.tamago.hunger.weight,
                      " \nОжирение: ", self.tamago.hunger.obestylv,
                      " \nРадость: ", self.tamago.happy.happylv,
                      f" \nБолезнь: {'да' if self.tamago.health.healthst == 0 else 'нет'}")

            #Действие 2
            elif self.move == "2":

                self.tamago.hunger.Eat()

            #Действие 3
            elif self.move == "3":

                if self.tamago.health.healthst == 1:

                    print("\nЛечение не нужно")

                else:

                    self.tamago.health.Regen()

            #Выход из программы
            elif self.move == "ext":

                self.tamago.Dead()

            #Минимальная обработка исключений в случае неправильно введёной команды
            else:

                print("\nКоманда введена неверно")

#Запуск программы если файл называется main
if __name__ == '__main__':
    UI()
