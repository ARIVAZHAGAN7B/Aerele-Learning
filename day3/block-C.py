'''Learned nameSpace, SOLID principles'''

# 1. Modules work as namespaces
# ================================

import math as m

a = m.sqrt(25)
b = m.pi

print(a)
print(b)


# 2. Function > Single-method class
# ==========================================

# Unnecessary class
class Add:
    def run(self, a, b):
        return a + b

x = Add()
print(x.run(2, 3))

# Better
def add(a, b):
    return a + b

print(add(2, 3))


# SOLID Principles (Python Style)
# ==========================================

# S - Single Responsibility

class User:
    def __init__(self, n):
        self.n = n

class Save:
    def save(self, u):
        print("Saved", u.n)

u = User("Tom")
Save().save(u)


# O - Open/Closed

class Shape:
    def area(self):
        raise NotImplementedError

class Sq(Shape):
    def __init__(self, a):
        self.a = a

    def area(self):
        return self.a * self.a

class Cir(Shape):
    def __init__(self, r):
        self.r = r

    def area(self):
        return 3.14 * self.r * self.r

for s in [Sq(4), Cir(2)]:
    print(s.area())



# L - Liskov Substitution


class Bird:
    def sound(self):
        print("bird")

class Crow(Bird):
    def sound(self):
        print("caw")

def f(a):
    a.sound()

f(Bird())
f(Crow())



# I - Interface Segregation


class Print:
    def p(self):
        print("print")

class Scan:
    def s(self):
        print("scan")

class Mfp(Print, Scan):
    pass

x = Mfp()
x.p()
x.s()


# D - Dependency Inversion

class MySQL:
    def save(self):
        print("mysql")

class Mongo:
    def save(self):
        print("mongo")

class App:
    def __init__(self, d):
        self.d = d

    def run(self):
        self.d.save()

App(MySQL()).run()
App(Mongo()).run()