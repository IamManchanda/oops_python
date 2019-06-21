class Animal:
    cool = True

    def make_sound(self, sound):
        return f"The Animal says {sound}"

class Cat(Animal):
    pass

blue = Cat()
print(blue.make_sound("Meoww..."))
print(blue.cool)
print(Cat.cool)
print(Animal.cool)

print(isinstance(blue, Cat))
print(isinstance(blue, Animal))
