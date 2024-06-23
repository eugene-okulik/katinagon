import random

salary = int(input('Введите salary: '))
bonus = bool(random.randint(0, 1))

if bonus:
    print(f"{salary}, {bonus} - '${salary + int(random.random() * 100)}'")
else:
    print(f"{salary}, {bonus} - '${salary}'")
