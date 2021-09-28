class Octopus:
    count_animals = 0

    def __init__(self, name="Octavio"):
        self._name = name
        self._age = 0

    def birthday(self):
        self._age += 1

    def get_age(self):
        return self._age

    def set_name(self, name):
        self._name = name

    def get_name(self):
        return self._name


def main():
    o1 = Octopus("octopus")
    Octopus.count_animals += 1
    o2 = Octopus()
    Octopus.count_animals += 1
    print(o1.get_name())
    print(o2.get_name())
    o2.set_name("O")
    print(o2.get_name())
    print(Octopus.count_animals)


main()
