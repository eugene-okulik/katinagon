def result(sentences):
    words = sentences.split()
    return int(words[-1]) + 10


text_list = ['результат операции: 42', 'результат операции: 54', 'результат работы программы: 209',
             'результат: 2']

for text in text_list:
    print(result(text))
