from mainprocesses.tamago import Tamago
from mainprocesses.dead import DeadMenager

class UI:

    def __init__(self):

        self.name = input('введите имя: ')
        self.tamago = Tamago(self.name)
        self.Display()

    def Display(self):

        print('\nИмя питомца: ', self.name)
        self.tamago.Live()
        self.Game()

    def Game(self):

        while DeadMenager.alive():

            self.move = input("\nВведите действие: "
                              "\nУзнать информацию [1], "
                              "\nПокормить [2], "
                              "\nВылечить [3], "
                              "\nЗакончить игру [ext] ").lower()

            if self.move == "1":

                print("\nВозраст: ", self.tamago.age,
                      " \nЗдоровье: ", self.tamago.health.healthlv,
                      " \nВес: ", self.tamago.hunger.weight,
                      " \nОжирение: ", self.tamago.hunger.obestylv,
                      " \nРадость: ", self.tamago.happy.happylv,
                      f" \nБолезнь: {'да' if self.tamago.health.healthst == 0 else 'нет'}")

            elif self.move == "2":

                self.tamago.hunger.Eat()

                print("\nВы покормили ", self.name,
                      "\nВес: ", self.tamago.hunger.weight,
                      "\nОжирение: ", self.tamago.hunger.obestylv,
                      "\nРадость: ", self.tamago.happy.happylv)

            elif self.move == "3":

                if self.tamago.health.healthst == 1:

                    print("\nЛечение не нужно")

                else:

                    self.tamago.health.Regen()

            elif self.move == "ext":

                self.tamago.Dead()

            else:

                print("\nКоманда введена неверно")


if __name__ == '__main__':
    UI()
