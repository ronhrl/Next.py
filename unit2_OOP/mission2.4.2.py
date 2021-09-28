class BigThing:
    def __init__(self, size):
        self._size = size

    def size(self):
        if isinstance(self._size, int):
            return self._size
        elif isinstance(self._size, list):
            return len(self._size)
        elif isinstance(self._size, dict):
            return len(self._size)
        elif isinstance(self._size, str):
            return len(self._size)


class BigCat(BigThing):
    def __init__(self, size, weight):
        super(BigCat, self).__init__(size)
        self.weight = weight

    def size(self):
        super()
        if 15 < self.weight < 20:
            return "Fat"
        elif self.weight > 20:
            return "Very Fat"
        else:
            return "OK"


def main():
    my_thing = BigThing("balloon")
    print(my_thing.size())
    cutie = BigCat("mitzy", 22)
    print(cutie.size())


main()
