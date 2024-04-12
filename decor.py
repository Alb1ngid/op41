import time


def func_decor(func):
    def wrapper(*args, **kwargs):
        dt=time.time()
        func(*args, **kwargs)
        at = time.time()
        print(f'время работы функции { dt-at} ')
    return wrapper

@func_decor
def some_func(title,tag):
    a=3999-1938392
    print(title,tag)
    return f'{tag} {title} {tag}'

# some_func('hello','world')
print(some_func('hello','world'))