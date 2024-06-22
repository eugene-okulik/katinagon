import sys
sys.set_int_max_str_digits(0)


def fibonacci_fun():
    numbers = [1, 1]
    while True:
        yield numbers[-1]
        numbers.append(numbers[-1] + numbers[-2])


count = 2
n = [5, 200, 1000, 100000]
for number in fibonacci_fun():
    if count in n:
        print(number)
        if count == n[-1]:
            break
    count += 1
