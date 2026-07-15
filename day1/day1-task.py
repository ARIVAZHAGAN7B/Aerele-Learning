
#
#python -m venv venv -- starting Virutual environment
#source venv/bin/activate  -- activating


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

squares = [num ** 2 for num in numbers]

print(squares)

with open("squares.txt", "w") as file:
    for square in squares:
        file.write(f"{square}\n")

with open("squares.txt") as file:
    text = file.read()
    print(text)

t = [(1, 2), (1,), (3, 4)]

for item in t:
    try:
        k, v = item
        print(k, v)
    except ValueError:
        print(f"Skipping invalid item: {item}")