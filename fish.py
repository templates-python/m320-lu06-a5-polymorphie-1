from animal import Animal


class Fish(Animal):

    def __init__(self, species, name):
        super().__init__(species)
        self.__name = name

    def move(self):
        print(self._species + " mit Name " + self.__name + " schwimmt")