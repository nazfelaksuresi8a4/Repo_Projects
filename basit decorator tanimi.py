def decorator(func):
    def wrapper():
        print('started')
        print(func())
        print('ended')
        return func
    return wrapper()

@decorator
def myfunc():
    return abs(((-2) ** 2) * 4 * ((4 ** (4 * 16 / 2) / 2) * (4 * 4)))

outMain = myfunc()
print(outMain)
