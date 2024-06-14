my_dict = {'tuple': (100, 200, 300, 400, 500),
           'list': ['one', 'two', 'three', 'four', 'five'],
           'dict': {'январь': 1, 'февраль': 2, 'март': 3, 'апрель': 4, 'май': 5},
           'set': {'a', 'b', 'c', 'd', 'e'}
           }
print(my_dict['tuple'][-1])
my_dict['list'].append('six')
my_dict['list'].pop(1)
my_dict['dict']['i am a tuple'] = 'кортеж'
my_dict['dict'].pop('март')
my_dict['set'].add('f')
my_dict['set'].pop()
print(my_dict)
