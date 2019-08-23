"""
map filter
"""
a = [i for i in range(0, 10)]
print(f'a: {a}')
print(list(filter(lambda x: x % 2 == 1, a)))
print(list(map(lambda x: x * 2, a)))

"""
sorted
"""
dt = dict(a=32, b=21, c=31)
print(sorted(dt.items(), key=lambda x: x[1], reverse=False))
print(sorted(dt.items(), key=lambda x: x[0], reverse=True))