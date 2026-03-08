a,b = 4,2

def mainfnc(a,b):
    res = (a**b) - (b**2)
    print(res)
    return res


def wrapper(myfncc):
    print('dx1')
    res = myfncc(a,b)
    print('dx2')
    return res 


decorator_out = wrapper(mainfnc)

print(decorator_out)
