""" Python classes """

class Cricketer:
    active_cricketers = 0

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        Cricketer.active_cricketers += 1

    def full_name_with_age(self):
        return f"{self.first_name} {self.last_name} is {self.age} years old now."
    
    def best_shot(self, thing):
        return f"{self.first_name}'s best shot is {thing}."

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

print(f"\nCurrent Active Cricketers: {Cricketer.active_cricketers}")

print("\n")
cricketer1 = Cricketer("Sourav", "Ganguly", 46)
print(cricketer1.best_shot("Off Drive"));
print(cricketer1.full_name_with_age());
print(cricketer1.happy_birthday());
print(cricketer1.full_name_with_age());

print("\n")
cricketer2 = Cricketer("MS", "Dhoni", 37)
print(cricketer2.best_shot("Helicopter Shot"));
print(cricketer2.full_name_with_age());
print(cricketer2.happy_birthday());
print(cricketer2.full_name_with_age());

print("\n")
cricketer3 = Cricketer("Virat", "Kohli", 30)
print(cricketer3.best_shot("Cover Drive"));
print(cricketer3.full_name_with_age());
print(cricketer3.happy_birthday());
print(cricketer3.full_name_with_age());

print("\n")
print(f"Current Active Cricketers: {Cricketer.active_cricketers}")

print("\n")
print(cricketer1.retirement());
print(f"Current Active Cricketers: {Cricketer.active_cricketers}")

print("\n")
