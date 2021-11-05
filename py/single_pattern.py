import time


def singleton(cls):
    instances = {}

    def wrapper(*args, **kwargs):
        if cls not in instances:
            print('start ')
            instances[cls] = cls(*args, **kwargs)
            print('end ')
        return instances[cls]

    return wrapper


@singleton
class Foo(object):
    def __init__(self):
        time.sleep(4)
    pass


foo1 = Foo()
foo2 = Foo()
print(foo1 is foo2)  # True
