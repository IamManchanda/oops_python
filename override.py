class Animal:
    def speak(self):
        raise NotImplementedError("Subclass needs to implement this method")

class Dog(Animal):
    def speak(self):
        return "Woof..."

class Cat(Animal):
    def speak(self):
        return "Meow..."

class Fish(Animal):
    pass

print("\n")
d = Dog()
print(d.speak())

print("\n")
f = Fish()
print(f.speak())
