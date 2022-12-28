from pet import Pet
class Ninja:

    def __init__(self, first_name, last_name, pet, treats, pet_food):
        self.first_name = first_name
        self.last_name = last_name
        self.pet = pet
        self.treats = treats
        self.pet_food = pet_food

    def walk(self):
        self.pet.play()
        print("All tuckered out from a walk")
        return self

    def feed(self):
        self.pet.eat()
        print("Feeding dog")
        return self

    def bathe(self):
        self.pet.makes_noise()
        print("Cleaning Dog")
        return self

    def checkup(self):
        self.pet.vet()
        print("Vet takes a look")
        return self

Bella = Pet("Bella", "Deer", "Hide", "Bonk")
Charlie = Pet("Charlie", "Chihuahua", "Spin", "Yip")
some_treats = ["Greenies", "Bone", "Pizza"]
some_food = ["Wet Food", "Dry Food", "People Food"]

Ninja_1 = Ninja("Brendan", "Cordova", Charlie, some_treats, some_food)
Ninja_2 = Ninja("Tori", "Cordova", Bella, some_treats, some_food)

#pet_1
print(Ninja_1)
Ninja_1.walk().feed().checkup().walk().walk().checkup()
Ninja_1.bathe().feed().checkup()

#pet_2
print(Ninja_2)
Ninja_2.walk().feed().checkup().walk().walk().checkup()
Ninja_2.bathe().feed().checkup()