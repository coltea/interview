def single_pattern(cls):
    cls_dt = dict()

    def wrapper(*args, **kwargs):
        if cls not in cls_dt:
            cls_dt[cls] = cls(*args, **kwargs)
        return cls_dt[cls]

    return wrapper


class Foo(object):
    pass


f1 = Foo()
f2 = Foo()
print(f1 == f2)


@single_pattern
class Foo2(object):
    pass


f1 = Foo2()
f2 = Foo2()
print(f1 == f2)
