def func(a, b=2, *args, c=3, **kwargs):
    print(a, b, args, c, kwargs)



func(1, 5, 10, 20, name='Tom', c=30)