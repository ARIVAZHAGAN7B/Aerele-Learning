from ..block_B.calculator import Calculator

calc = Calculator()

result_add = calc.add(10, 5)
result_subtract = calc.subtract(10, 5)
result_multiply = calc.multiply(10, 5)
try:
    result_divide = calc.divide(10, 0)
except ValueError as e:
    result_divide = str(e)

print(f"Addition Result: {result_add}")
print(f"Subtraction Result: {result_subtract}")
print(f"Multiplication Result: {result_multiply}")
print(f"Division Result: {result_divide}")