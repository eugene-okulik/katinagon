def repeat_me(func):
    def wrapper(*args, count):
        counter = 0
        while counter < count:
            func(*args)
            counter += 1
    return wrapper


def repeat_me2(count):
    def inner_func(func):
        def wrapper(*args):
            counter = 0
            while counter < count:
                func(*args)
                counter += 1
        return wrapper
    return inner_func


@repeat_me
def example(text):
    print(text)


@repeat_me2(count=3)
def example2(text):
    print(text)


example('print me', count=2)
example2('Hello')
