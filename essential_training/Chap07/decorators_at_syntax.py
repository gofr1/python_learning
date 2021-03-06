#!/usr/bin/env python3

def new_decorator(some_func):

    def wrap_the_function():
        print(f'I am doing some work before executing {some_func.__name__}')
        some_func()
        print(f'I am doing some work after executing {some_func.__name__}')

    return wrap_the_function

@new_decorator
def func_that_requires_decoration():
    print('I am the function which needs some decoration')

func_that_requires_decoration()
#* I am doing some work before executing func_that_requires_decoration
#* I am the function which needs some decoration
#* I am doing some work after executing func_that_requires_decoration

print(func_that_requires_decoration.__name__)
#* wrap_the_function
# func_that_requires_decoration is overrided by wrap_the_function