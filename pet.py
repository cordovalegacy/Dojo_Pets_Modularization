class Pet:

    def __init__(self, name, type, tricks, noise):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.noise = noise
        self. health = 100
        self.energy = 50

    def vet(self):
        print(f"{self.name} has {self.health} Health and {self.energy} Energy remaining")

    def sleep(self):
        self.energy = self.energy + 25
        print()
        return self

    def eat(self):
        self.energy = self.energy + 5
        self.health = self.health + 10
        return self

    def play(self):
        self.health = self.health + 5
        self.energy = self.energy - 10
        return self

    def makes_noise(self):
        self.health = self.health + 5
        self.energy = self.energy + 20
        print(self.noise)
        return self