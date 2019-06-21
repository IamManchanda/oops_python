""" Method Resolution Order (MRO) """

class A:
    def do_something(self):
        return "Method defined in: A"

class B(A):
    def do_something(self):
        return "Method defined in: B"

class C(A):
    def do_something(self):
        return "Method defined in: C"

class D(B, C):
    def do_something(self):
        return "Method defined in: D"

print(D.mro())
thing = D()
print(thing.do_something())
