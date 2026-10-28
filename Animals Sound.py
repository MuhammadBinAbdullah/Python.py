from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, name, habitat):
        self.name = name
        self.habitat = habitat

    def display(self):
        print(f"Name : {self.name} | Habitat : {self.habitat}")

    @abstractmethod
    def speak(self):
        pass

class Dog(Animal):

    def __init__(self, name, habitat, bread):
        super().__init__(name, habitat, breed)
        self.breed = breed

    def speak(self):
        print(f"{self.name} ({self.breed}) Says: Woof! Woof!")

class Parrot(Animal):

    def __init__(self, name, habitat, phrase):
        super().__init__(name, habitat)
        self.phrase = phrase

    def speak(self):
        print(f"{self.name} Says: {self.phrase}! {self.phrase}!")

class Lion(Animal):

    def __init__(self, name, habitat, pride):
        super().__init__(name, habitat)
        self.pride = pride

    def speak(self):
        print(f"{self.name} (Pride: {self.pride}) Says: ROARRR!")

dog    = Dog("Bruno", "Home", "Labrodor")
parrot = Parrot("Polly", "Jungle", "Squawk")
lion   = Lion("Simba", "Savannah", "Pride Rock")

print("=== Animal Sound Show ===\n")
for animal in [dog, parrot, lion]:
    animal.display()
    animal.speak()
    print()