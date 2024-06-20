number = 9
print('Угадайте цифру')
while True:
    user_number = int(input())
    if user_number == number:
        print('Поздравляю! Вы угадали!')
        break
    else:
        print('Попробуйте снова')
