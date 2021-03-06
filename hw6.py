class Anymals():

    def __init__(self, name, weight):
        self.name = name
        self.weight = weight
        self.satiety = 'hungry'

    def feed(self):
        self.satiety = 'not_hungry'

    # def fold_weight(self):
    #     for el in Anymals():
    #         sum_weight = 0
    #         sum_weight += self.weight

class Cows(Anymals):

    def __init__(self, name, weight):
        super().__init__(name, weight)
        self.milk = 'full'

    def get_milk(self):
        self.milk = 'not'

    def get_voice(self):
        print('Мууу!')

    def get_status(self):
        print(f'Имя - {self.name}, вес - {self.weight}, сытость - {self.satiety}, молоко - {self.milk}.')

    # def fold_weight(self):
    #     for Cows.weight in Cows:
    #         sum_weight = 0
    #         sum_weight += Cows.weight
    #     print(f'Масса всех коров - {sum_weight} кг')

class Geese(Anymals): #goose
    # self.list_weight = []

    def __init__(self, name, weight):
        super().__init__(name, weight)
        self.eggs = 'full'
        # self.list_weight = []
        # self.list_weight.append(weight)


    def get_eggs(self):
        self.eggs = 'not'

    def get_voice(self):
        print('Га-га-га!')

    def get_status(self):
        print(f'Имя - {self.name}, вес - {self.weight}, сытость - {self.satiety}, яйца - {self.eggs}.')

class Sheeps(Anymals): #овцы

    def __init__(self, name, weight):
        super().__init__(name, weight)
        self.wool = 'full'

    def get_wool(self):
        self.wool = 'not'

    def get_voice(self):
        print('Бее!')

    def get_status(self):
        print(f'Имя - {self.name}, вес - {self.weight}, сытость - {self.satiety}, шерсть - {self.wool}.')

class Chickens(Geese):

    def __init__(self, name, weight):
        super().__init__(name, weight)

    def get_voice(self):
        print('Ко-ко-ко!')

class Goats(Cows): #козы

    def __init__(self, name, weight):
        super().__init__(name, weight)

    def get_voice(self):
        print('Мее!')

class Ducks(Geese):

    def __init__(self, name, weight):
        super().__init__(name, weight)

    def get_voice(self):
        print('Кря-кря!')

cow_1 = Cows('Манька', 200)
cow_1.get_status()
cow_1.get_voice()
cow_1.feed()
cow_1.get_milk()
cow_1.get_status()

goose_1 = Geese('Серый', 6)
goose_1.get_status()
goose_1.get_voice()
goose_1.feed()
goose_1.get_eggs()
goose_1.get_status()
goose_2 = Geese('Белый', 7)
goose_2.get_status()
goose_2.get_voice()
goose_2.feed()
goose_2.get_eggs()
goose_2.get_status()

sheep_1 = Sheeps('Барашек', 80)
sheep_1.get_status()
sheep_1.get_voice()
sheep_1.feed()
sheep_1.get_wool()
sheep_1.get_status()
sheep_2 = Sheeps('Кудрявый', 90)
sheep_2.get_status()
sheep_2.get_voice()
sheep_2.feed()
sheep_2.get_wool()
sheep_2.get_status()

chicken_1 = Chickens('Ко-Ко', 3)
chicken_1.get_status()
chicken_1.get_voice()
chicken_1.feed()
chicken_1.get_eggs()
chicken_1.get_status()
chicken_2 = Chickens('Кукареку', 4)
chicken_2.get_status()
chicken_2.get_voice()
chicken_2.feed()
chicken_2.get_eggs()
chicken_2.get_status()

goat_1 = Goats('Рога', 70)
goat_1.get_status()
goat_1.get_voice()
goat_1.feed()
goat_1.get_milk()
goat_1.get_status()
goat_2 = Goats('Копыта', 80)
goat_2.get_status()
goat_2.get_voice()
goat_2.feed()
goat_2.get_milk()
goat_2.get_status()

duck_1 = Ducks('Кряква', 3)
duck_1.get_status()
duck_1.get_voice()
duck_1.feed()
duck_1.get_eggs()
duck_1.get_status()