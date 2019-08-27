def log(func):
    def wrapper(*args, **kw):
        print(f'call {func.__name__}():')
        return func(*args, **kw)
    return wrapper


@log
def now():
    print('2015-3-25')


if __name__ == '__main__':
    now()