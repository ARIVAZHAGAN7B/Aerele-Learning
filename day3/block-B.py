#learned inheritence, composition, MRO, Mixins, Dataclass, Enum, namedTuple, Dunder method

'''INHERITENCE'''

class grandParent:

    def __init__(self):
        self.grandparent_attr = "grandparent attribute"

    def method(self):
        return "grandparent method"

class parent(grandParent):
    
    def __init__(self):
        super().__init__()
        self.parent_attr = "parent attribute"

    def method(self):
        return super().method()

class child(parent):

    def __init__(self):
        super().__init__()
        self.child_attr = "child attribute"


print(child().method())



'''MRO'''

class A:

    def method(self):
        return "A method"
class B(A):
    def method(self):
        return "B method"

class C(A):
    def method(self):
        return "C method"

class D(C, B):
    def method(self):   
        return super().method()
    
class E(D):
    def method(self):
        return super().method()

d = D()
print(d.method())


"""MIXINS"""

class log:
    def log(self, message):
        print(f"Logging: {message}")

class payment(log):

    pass

class addedUser(log):
    pass

p = payment()
u = addedUser()
p.log("this payment successfull")
u.log("this is user interface")


'''DATACLASS'''

from dataclasses import dataclass

@dataclass
class main:
    name:str
    salary:int

m1 = main("ajith", 106)
m2 = main("ajith", 106)
print(m1==m2)


'''ENUM'''
from enum import Enum

class diff(Enum):
    PENDING = "pending"
    APPROVED = "approved"
    COMPLETED = "completed"

class checker:

    def __init__(self,status:diff):
        print(status.name)
status = diff.PENDING
c = checker(status)      



'''NAMEDTUPLE'''

from collections import namedtuple

Person = namedtuple("Person", "name id salary", defaults=[100000, 99, 'none'])
p = Person("Arivazhagan")
print(p)


'''DUNDER METHOD'''
@dataclass
class dunder_method:
    name:str
    number:int
    def __str__(self):
        return self.name + "this guy is jew" + str(self.number) + "having this as a number"

dm = dunder_method("Arivu", 10)
print(dm)