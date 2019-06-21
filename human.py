class Human:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        if age >= 0:
            self._age = age
        else:
            self._age = 0
    
    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if value >= 0:
            self._age = value
        else:
            raise ValueError("Age can't be negative")

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    @full_name.setter
    def full_name(self, value):
        (self.first_name, self.last_name) = value.split(" ")

harry = Human("Harry", "Manchanda", 25)
print(harry.age)
harry.age = 26
print(harry.age)
print(harry.full_name)
harry.full_name = "Harman Manchanda"
print(harry.first_name, harry.last_name, "|", harry.full_name)
print(harry.__dict__)
