class Dog:
    def __init__(self):
        self.name = "dogy"
        self.age = 0

    def birthday(self):
        self.age += 1

    def get_age(self):
        return self.age


def main():
    d1 = Dog()
    d1.birthday()
    d2 = Dog()
    d2.birthday()
    print(d1.get_age())
    print(d1.get_age())


main()
