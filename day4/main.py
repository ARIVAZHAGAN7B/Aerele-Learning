from .block_A.modules import result_add, result_subtract, result_multiply, result_divide
import sys

for p in sys.path:
    print(p)

print(f"Addition Result: {result_add}")
print(f"Subtraction Result: {result_subtract}")
print(f"Multiplication Result: {result_multiply}")
print(f"Division Result: {result_divide}")

print(type(10))
from .block_B.calculator import Calculator

calc = Calculator()
print(f"Calculator Result: {calc.add(10, 5)}")
