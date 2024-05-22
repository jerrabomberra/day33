def sum(p, *args, **kwargs):
    z = 1
    z *= p
    for i in args:
        z *= i
    for key, value in kwargs.items():
        z *= value
    return z


print(sum(2, 5, a=4, b=3))


my_list = list(map(lambda  :  ,  ))