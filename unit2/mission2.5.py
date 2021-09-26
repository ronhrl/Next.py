class Animal:
    zoo_name = "Hayaton"

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

    def talk(self):
        pass


class Dog(Animal):
    def get_name(self):
        return super().get_name()

    def is_hungry(self):
        return super().is_hungry()

    def feed(self):
        super().feed()

    def talk(self):
        print("woof woof")

    def fetch_stick(self):
        print("There you go, sir!")


class Cat(Animal):
    def get_name(self):
        return super().get_name()

    def is_hungry(self):
        return super().is_hungry()

    def feed(self):
        super().feed()

    def talk(self):
        print("meow")

    def chase_laser(self):
        print("Meeeow")


class Skunk(Animal):
    def __init__(self, name, hunger, stink_count=6):
        super().__init__(name, hunger)
        _stink_count = stink_count

    def get_name(self):
        return super().get_name()

    def is_hungry(self):
        return super().is_hungry()

    def feed(self):
        super().feed()

    def talk(self):
        print("tsssss")

    def stink(self):
        print("Dear lord")


class Unicorn(Animal):
    def get_name(self):
        return super().get_name()

    def is_hungry(self):
        return super().is_hungry()

    def feed(self):
        super().feed()

    def talk(self):
        print("Good day, darling")

    def sing(self):
        print("I'm not your toy...")


class Dragon(Animal):
    def __init__(self, name, hunger, color="Green"):
        super().__init__(name, hunger)
        _color = color

    def get_name(self):
        return super().get_name()

    def is_hungry(self):
        return super().is_hungry()

    def feed(self):
        super().feed()

    def talk(self):
        print("Raaaawr")

    def breath_fire(self):
        print("$@#$#@$")


def main():
    my_dog = Dog("Brownie", 10)
    cat = Cat("Zelda", 3)
    skunk = Skunk("Stinky", 0)
    unicorn = Unicorn("Keith", 7)
    dragon = Dragon("Lizzy", 1450)
    dog_doggo = Dog("Doggo", 80)
    cat_kitty = Cat("Kitty", 80)
    skunk_stinky = Skunk("Stinky Jr.", 80)
    unicorn_clair = Unicorn("Clair", 80)
    dragon_mc = Dragon("McFly", 80)
    zoo_lst = my_dog, cat, skunk, unicorn, dragon, dog_doggo, cat_kitty, skunk_stinky, unicorn_clair, dragon_mc
    for animal in zoo_lst:
        print(type(animal))
        print(animal.get_name())
        while animal.is_hungry():
            animal.feed()
        animal.talk()
        if isinstance(animal, Dog):
            animal.fetch_stick()
        elif isinstance(animal, Cat):
            animal.chase_laser()
        elif isinstance(animal, Skunk):
            animal.stink()
        elif isinstance(animal, Unicorn):
            animal.sing()
        elif isinstance(animal, Dragon):
            animal.breath_fire()

    print(Animal.zoo_name)


if __name__ == "__main__":
    main()
