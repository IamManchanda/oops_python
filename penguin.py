class Aquatic:
    def __init__(self, name):
        self.name = name

    def swim(self):
         return f"{self.name} is swimming"

    def greet(self):
         return f"I am {self.name} of the sea"

class Ambulatory:
    def __init__(self, name):
        self.name = name

    def walk(self):
         return f"{self.name} is walking"

    def greet(self):
         return f"I am {self.name} of the land"

class Penguin(Aquatic, Ambulatory):
    def __init__(self, name):
        super().__init__(name = name)

jaws = Aquatic("Jaws")
lassie = Ambulatory("Lassie")
captain_cook = Penguin("Captain Cook")

print("\n")
print(jaws.swim())
print(jaws.greet())

print("\n")
print(lassie.walk())
print(lassie.greet())

print("\n")
print(captain_cook.swim())
print(captain_cook.walk())
print(captain_cook.greet())

print("\n")
