class Counter:
    __ncreated = 0

    def __init__(self, color="black", initValue=0) -> None:
        self.__count = initValue
        self.__color = color

    def reset(self):
        self.__count = 0

    def increment(self):
        self.__count += 1

    def get(self):
        return self.__count

    def __eq__(self, other) -> bool:
        return self.__count == other.__count

    def __str__(self):
        return "hello"


a = Counter(100)
b = Counter
print(a)
