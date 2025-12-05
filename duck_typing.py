class Animal:
    alive = True

class Dog(Animal):
    def speak(self):
        print("WOOF!")

class Cat(Animal):
    def speak(self):
        print("MEOW!")

class car:
    alive = False
    def speak(self):
        print("Honk!")

animal = [Dog(), Cat(), car()]

for animal in animal:
    animal.speak()
    print(animal.alive)
