class Animals:

    def __init__(self, name):
        self.name = name
        print(self.name + " animal was born")

    def makeNoise(self):
        print(self.name + " said Argh!")

    def eat(self):
        print("Chavk")


class Cats(Animals):

    def __init__(self, name):
        self.name = name
        print(self.name + " cat was born")
        super().__init__(name)

    def makeNoise(self):
        print(self.name + " said MEOW!")

    def eat(self):
        print("Chavk")


class Dogs(Animals):

    def __init__(self, name):
        self.name = name
        print(self.name + " dog was born")
        super().__init__(name)

    def makeNoise(self):
        print(self.name + " said WOUF!")

    def eat(self):
        print("chavk")