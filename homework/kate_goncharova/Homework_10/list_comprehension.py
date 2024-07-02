PRICE_LIST = '''тетрадь 50р
книга 200р
ручка 100р
карандаш 70р
альбом 120р
пенал 300р
рюкзак 500р'''

words_list = PRICE_LIST.split()
list_with_price = [int(words_list[i][:-1]) for i in range(len(words_list)) if i % 2 != 0]
words_list = [words_list[i] for i in range(len(words_list)) if i % 2 == 0]
new_dict = {key: value for key, value in zip(words_list, list_with_price)}
print(new_dict)
