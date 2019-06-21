""" Python classes """

class Cricketer:
    active_cricketers = 0

    @classmethod
    def display_active_cricketers(cls):
        return cls.active_cricketers

    def __init__(self, first_name, last_name, age, cup_year):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.cup_year = cup_year
        Cricketer.active_cricketers += 1

    def __repr__(self):
        return f"World Cup {self.cup_year} is ours {self.first_name} {self.last_name}";

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    @full_name.setter
    def full_name(self, value):
        (self.first_name, self.last_name) = value.split(" ")

    def full_name_with_age(self):
        return f"{self.first_name} {self.last_name} is {self.age} years old now."
    
    def best_shot(self, thing):
        return f"{self.first_name}'s best shot: {thing}."

    def happy_birthday(self):
        self.age += 1
        if self.age % 10 == 1:
            greet = "st"
        elif self.age % 10 == 2:
            greet = "nd"
        elif self.age % 10 == 3:
            greet = "rd"
        else:
            greet = "th"
        return f"Happy {self.age}{greet} Birthday, {self.first_name}"

    def retirement(self):
        Cricketer.active_cricketers -= 1
        return f"{self.first_name} {self.last_name} has retired."

class Coach(Cricketer):
    active_coaches = 0

    @classmethod
    def display_active_coaches(cls):
        return cls.active_coaches

    def __init__(self, first_name, last_name, age, cup_year, coaching_role):
        super().__init__(first_name, last_name, age, cup_year)
        self.coaching_role = coaching_role
        Coach.active_coaches += 1

    def announce_coaching_role(self):
        return f"{self.full_name} is now Team India's {self.coaching_role}"

print(f"\nCurrent Active Cricketers: {Cricketer.display_active_cricketers()}")

print("\n")
kapil = Cricketer("Kapil", "Dev", 60, 1983)
print(kapil)
print(kapil.best_shot("Nataraja Shot"));
print(kapil.full_name_with_age());
print(kapil.happy_birthday());
print(kapil.full_name_with_age());
print(f"Current Active Cricketers: {Cricketer.display_active_cricketers()}")

print("\n")
mahi = Cricketer("MS", "Dhoni", 37, 2011)
print(mahi)
print(mahi.best_shot("Helicopter Shot"));
print(mahi.full_name_with_age());
print(mahi.happy_birthday());
print(mahi.full_name_with_age());
print(f"Current Active Cricketers: {Cricketer.display_active_cricketers()}")

print("\n")
virat = Cricketer("Virat", "Kohli", 30, 2019)
print(virat)
print(virat.best_shot("Cover Drive"));
print(virat.full_name_with_age());
print(virat.happy_birthday());
print(virat.full_name_with_age());
print(f"Current Active Cricketers: {Cricketer.display_active_cricketers()}")

print("\n")
print(kapil.retirement());
print(f"Current Active Cricketers: {Cricketer.display_active_cricketers()}")

print("\n")
ravi = Coach("Ravi", "Shashtri", 57, 2019, "Head Coach")
print(ravi)
print(ravi.best_shot("Chapati Shot"));
print(ravi.full_name_with_age());
print(ravi.happy_birthday());
print(ravi.full_name_with_age());
print(ravi.announce_coaching_role())
print(f"Current Active Cricketers: {Cricketer.display_active_cricketers()}")
print(f"Current Active Coaches: {Coach.display_active_coaches()}")

print("\n")