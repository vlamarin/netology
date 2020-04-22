class Anymals():

    def __init__(self, name, weight):
        self.name = name
        self.weight = weight
        self.satiety = 'hungry'

    def satiety(self):
        self.satiety = 'not_hungry'

    def sum_weight(self):
        self.sum_weight = sum(self.weight)

class Cows(Anymals):

    def __init__(self, name, weight):
        super().__init__(name, weight)
        self.milk = 'full'

    def get_milk(self):
        self.milk = 'not'

    def get_voice(self):
        print('Мууу!')

class Geese(): #goose
    pass

class Sheeps(): #овцы
    pass

class Chickens():
    pass

class Goats(): #козы
    pass

class Ducks():
    pass

cow_1 = Cows('Манька', 200)
cow_1.satiety()
