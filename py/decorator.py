def log(func):
    def wrapper(*args, **kw):
        print(f'call {func.__name__}():')
        return func(*args, **kw)
    return wrapper


@log
def now():
    print('2015-3-25')


def get(function):
    def wrapper(*arg, **kwargs):
        return function(*arg, **kwargs)
    return wrapper


if __name__ == '__main__':
    now()


def get(function):
    def wrapper(*args, kwargs):
        return function(*args, **kwargs)
    return wrapper


