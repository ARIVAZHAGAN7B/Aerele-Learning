from typing import overload, override

class Base:
    @overload
    def greet(self, name: str) -> str:
        ...

    @overload
    def greet(self, name: int) -> str:
        ...

    def greet(self, name):
        if isinstance(name, str):
            return f"Hello, {name}!"
        elif isinstance(name, int):
            return f"Hello, user #{name}!"
        else:
            raise TypeError("Invalid type for name")

class Derived(Base):
    @override
    def greet(self, name: str) -> str:
        return f"Hi, {name}! Welcome to the derived class."

    @override
    def greet(self, name: int) -> str:
        return f"Hi, user #{name}! Welcome to the derived class."

if __name__ == "__main__":

    base = Base()
    print(base.greet("Alice"))  # Output: Hello, Alice!
    print(base.greet(42))       # Output: Hello, user #42!

    derived = Derived()
    print(derived.greet("Bob"))  # Output: Hi, Bob! Welcome to the derived class.
    print(derived.greet(99))     # Output: Hi, user #99! Welcome to the derived class.