# Моя зверушка
# Виртуальный питомец, о котором пользователь может заботиться
class Critter(object):  # создаем класс
    """Виртуальный питомец"""
    # инициализация 3х аттрибутов (2 из которых со значениями по умолчанию)
    def __init__(self, name, hunger = 0, boredom = 0): 
        self.name = name
        self.hunger = hunger
        self.boredom = boredom
    # закрытый (приватный) метод имитирующий течение времени.
    # будет вызваться из других методов
    def __pass_time(self):
        self.hunger += 1
        self.boredom += 1
    # свойство "настроение"
    @property # декоратор
    def mood(self):
        unhappiness = self.hunger + self.boredom
        if unhappiness < 5:
            m = "прекрасно"
        elif 5 <= unhappiness <= 10:
            m = "неплохо"
        elif 11 <= unhappiness <= 15:
            m = "не сказать чтобы хорошо"
        else:
            m = "ужасно"
        return m 
    
    def talk(self):
        print("Меня зовут", self.name, ", и сейчас я чувствую себя", self.mood, ".\n")
        self.__pass_time()
    # Кормление - уменьшает уровень голода
    def eat(self, food = 4):
        print("Мррр... Спасибо!")
        self.hunger -= food
        if self.hunger < 0:
            self.hunger = 0
        self.__pass_time()
    # Игра - уменьшает уровень скуки
    def play(self, fun = 4):
        print("Уиии!")
        self.boredom -= fun
        if self.boredom < 0:
            self.boredom = 0
        self.__pass_time()

def main():
    # создание зверушки
    crit_name = input("Как вы назовете свою зверушку? ")
    crit = Critter(crit_name)
    # меню
    choice = None
    while choice != "0":
        print \
            ("""
            Моя зверушка
            0 - Выйти
            1 - Узнать о самочувствии зверушки
            2 - Покормить зверушку
            3 - Поиграть со зверушкой
            """)
        choice = input("Ваш выбор: ")
        print()
        # выход
        if choice == "0":
            print("До свидания.")
        # беседа со зверушкой
        elif choice == "1":
            crit.talk()
        # кормление зверушки
        elif choice == "2":
            crit.eat()
        # игра со зверушкой
        elif choice == "3":
            crit.play()
        # непонятный пользовательский ввод
        else:
            print("Извините, в меню нет пункта", choice)

main()


    
