#Class design
class Animal:
    def action(self):
        pass  

#First subclass continuing downwards
class Dog(Animal):
    def action(self):
        return "Barking!" #overwritting from the blank action in class design

class Cat(Animal):
    def action(self):
        return "Meowing"

class Bird(Animal):
    def action(self):
        return "Chirping"

class Hyena(Animal):
    def action(self):
        return "laughing"

# Instance usage
animals = [Dog(), Cat(), Bird(), Hyena()]

for animal in animals:
    print(f"{animal.__class__.__name__}: {animal.action()}") #dispalys sounds for each animal aforementioned