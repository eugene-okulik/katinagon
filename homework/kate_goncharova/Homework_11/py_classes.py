class Book:
    material = 'бумага'
    presence_of_text = True

    def __init__(self, book_name, author, number_of_pages, isbn, is_reserved):
        self.book_name = book_name
        self.author = author
        self.number_of_pages = number_of_pages
        self.isbn = isbn
        self.is_reserved = is_reserved


class SchoolBook(Book):

    def __init__(self, book_name, author, number_of_pages, isbn, is_reserved, subject, school_class,
                 availability_of_tasks):
        super().__init__(book_name, author, number_of_pages, isbn, is_reserved)
        self.subject = subject
        self.school_class = school_class
        self.availability_of_tasks = availability_of_tasks


def print_book_list(input_list):
    for book in input_list:
        print(f"Название: {book.book_name}, Автор: {book.author}, страниц: {book.number_of_pages}", end='')
        if isinstance(book, SchoolBook):
            print(f", предмет: {book.subject}, класс: {book.school_class}", end='')
        elif isinstance(book, Book):
            print(f", материал: {book.material}", end='')
        if book.is_reserved:
            print(", зарезервирована", end='')
        print()


book_onegin = Book('Евгений Онегин', 'А. Пушкин', 288,
                   '978-5-4330-0181-7', False)
book_harry_potter = Book('Гарри Поттер и Тайная комната', 'Дж.К. Роулинг', 480,
                         '978-5-389-07781-2', False)
book_shining = Book('Сияние', 'С. Кинг', 544,
                    '978-5-17-080493-1', True)
book_lord_of_the_flies = Book('Повелитель мух', 'У. Голдинг', 320,
                              '978-5-17-103597-6', False)
book_crime_and_punishment = Book('Преступление и наказание', 'Ф. Достоевский', 608,
                                 '978-5-389-04926-0', False)
school_book_algebra9 = SchoolBook('Математика: алгебра и начала математического анализа',
                                  'М. Шабунина', 465, '978-5-09-116443-5', False,
                                  'математика', 9, True)
school_book_biology5 = SchoolBook('Биология. Введение в биологию', 'В. Пасечник', 177,
                                  '978-5-09-101351-1', False, 'биология', 5,
                                  False)
school_book_history6 = SchoolBook('История. Всеобщая история. История Средних веков', 'С. Тырин',
                                  273, '978-5-09-116490-9', True, 'история',
                                  6, False)

list_of_book = [book_onegin, book_harry_potter, book_shining, book_lord_of_the_flies, book_crime_and_punishment]
list_of_school_book = [school_book_algebra9, school_book_biology5, school_book_history6]

print_book_list(list_of_book)
print_book_list(list_of_school_book)
