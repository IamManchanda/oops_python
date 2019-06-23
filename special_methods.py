class Human:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def __repr__(self):
        return f"Human named {self.first_name} {self.last_name}"

    def __len__(self):
        return self.age

    def __add__(self, other):
        if isinstance(other, Human):
            return Human(first_name = "New Born", last_name = self.last_name, age = 0)
        return "You can't add that."

k = Human("Kevin", "Jones", 49)
l = Human("Lara", "Larsen", 47)

print("\n")
print(k)
print("Age:", len(k))

print("\n")
print(l)
print("Age:", len(l))

print("\n")
print(k + l)
print("Age:", len(k + l))

print("\n")
