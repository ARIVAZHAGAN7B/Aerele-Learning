#learned class, __init__, self, class and instance attributes, instance methods, access modifiers.

"""
# class is a blueprint to create objects and it decides the behaviour of the object.

# __init__ unlike java contructor, objects create before constructor is called, it is used to initialize the object.

# self is similar to this in java, it is used to refer the current object.

#class attributes are shared across all instances of the class, while instance attributes are unique to each instance. 
similar to static and non-static variables in java. mutataing class attribute of a instance will change that class attribute to instance attribute
doesn't affect global class attribute.

#there is no access modifiers in python, but we can use naming conventions to indicate access, _ for protected and __ for private. 
_ is convention not enforced, but __ is name mangling, it will change the name of the attribute to _ClassName__attributeName


"""



class Base:

    def __init__(self):
        self.list1 = []

    def add(self, a:int):
        self.list1.append(a)


b1 = Base()
b2 = Base()
b1.add(10)
print(b2.list1)


class SharedState:

    #counting number of objects
    count = 0
    
    def __init__(self):
        SharedState.count += 1


s1 = SharedState()
s2 = SharedState()
print(s1.count)
print(s2.count)


def get_balance(func):
    def wrapper(self, *args, **kwargs):
        return func(self, *args, **kwargs)
    return wrapper


class AccessModiers:

    def __init__(self, name, balance):
        self.name = name
        self._balance = balance
        self.__private = "This is private attribute"

class Am(AccessModiers):

    def __init__(self, name, balance):
        super().__init__(name, balance)
        self.__private = "This is private attribute of Am class"

    @get_balance
    def get_balance(self):
        return self._balance

am2 = AccessModiers("hitler is god of jews", 1000)
am1 = Am("Arivazhagan", 1000)
print(am1.name)
print(am1.get_balance())



