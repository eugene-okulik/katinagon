def select_operation(func):
    def wrapper(num1, num2):
        if num1 == num2:
            print(func(num1, num2, operation='+'))
        elif num1 > num2 >= 0 and num1 >= 0:
            print(func(num1, num2, operation='-'))
        elif num2 > num1 >= 0 and num2 >= 0:
            print(func(num1, num2, operation='/'))
        elif num1 < 0 or num2 < 0:
            print(func(num1, num2, operation='*'))
    return wrapper


@select_operation
def calc(first, second, operation):
    if operation == '+':
        return first + second
    elif operation == '-':
        return first - second
    elif operation == '*':
        return first * second
    elif operation == '/':
        return first / second


number1 = int(input('Введите первое число: '))
number2 = int(input('Введите второе число: '))
calc(number1, number2)
