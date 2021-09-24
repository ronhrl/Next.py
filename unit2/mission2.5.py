class Animal:
    def __init__(self, name, hunger=0):
        self._name = name
        self._hunger = hunger

    def get_name(self):
        return self._name

    def is_hungry(self):
        if self._hunger > 0:
            return True
        else:
            return False

    def feed(self):
        self._hunger -= 1


class Dog(Animal):
    def get_name(self):
        super()

    def is_hungry(self):
        super()

    def feed(self):
        super()


class Cat(Animal):
    def get_name(self):
        super()

    def is_hungry(self):
        super()

    def feed(self):
        super()


class Skunk(Animal):
    def get_name(self):
        super()

    def is_hungry(self):
        super()

    def feed(self):
        super()


class Unicorn(Animal):
    def get_name(self):
        super()

    def is_hungry(self):
        super()

    def feed(self):
        super()


class Dragon(Animal):
    def get_name(self):
        super()

    def is_hungry(self):
        super()

    def feed(self):
        super()


def main():
    animal = Animal("abc", 2)
    print(type(animal))
    print(animal.get_name())
    dog = Dog("Brownie", 10)
    cat = Cat("Zelda", 3)
    skunk = Skunk("Stinky", 0)
    unicorn = Unicorn("Keith", 7)
    dragon = Dragon("Lizzy", 1450)
    zoo_lst = (dog, cat, skunk, unicorn, dragon)
    for animal in zoo_lst:
        print(type(animal))
        print(animal.get_name())
        while animal.is_hungry():
            animal.feed()


main()
