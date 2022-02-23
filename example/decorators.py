"""
Basic stuff on how decorators can work in Python.

Covers:


"""

import functools
from multiprocessing.sharedctypes import Value
import time
import math
import random

#simple decorator
def simple_decorator(func):
    def wrapper():
        print("BEFORE the function call")
        func()
        print("AFTER the function call\n")
    return wrapper

@simple_decorator
def simple_function():
    print("This is the simple function")

simple_function()

#decorating functions with arguments
def arg_kwarg_decorator(func):
    def wrapper(*args, **kwargs):
        print("BEFORE the function call")
        func(*args, **kwargs)
        print("AFTER the function call\n")
    return wrapper

@arg_kwarg_decorator
def arg_kwarg_function(year, advice='don\'t get mugged!'):
    print(f'The year is {year}, {advice}')

arg_kwarg_function(2022, advice='stay alive!')

#returning values from decorated functions
def return_decorator(func):
    def wrapper_do_twice(*args, **kwargs):
        print('This went through the return decorator')
        return func(*args, **kwargs)
    return wrapper_do_twice

@return_decorator
def current_time():
    return str(time.time()) + " seconds since Jan 1, 1970\n"

print(current_time())

#function, but it decorating it does not confuse its 'identity'
def remember_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

@remember_decorator
def formatted_time():
    return time.asctime()

formatted_time()
print(formatted_time(), formatted_time.__name__, sep="\n")

#timing functiosn
def timer(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        delta = end - start
        print(f"Finished {func.__name__!r} in {delta:.4f} secs")
        return result
    return wrapper

@timer
def useless_calculations(n=15_000_000):
    sum([i for i in range(n)])

useless_calculations()

print()

#uses in debugging
def debug(func):
    """Print the function signature and return value"""
    @functools.wraps(func)
    def wrapper_debug(*args, **kwargs):
        args_repr = [repr(a) for a in args]                      # 1
        kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]  # 2
        signature = ", ".join(args_repr + kwargs_repr)           # 3
        print(f"Calling {func.__name__}({signature})")
        value = func(*args, **kwargs)
        print(f"{func.__name__!r} returned {value!r}")           # 4
        return value
    return wrapper_debug

@debug
def make_greeting(name, age=None):
    if age is None:
        return f"Howdy {name}!"
    else:
        return f"Whoa {name}! {age} already, you are growing up!"

print(make_greeting('Peter Parker', age=21), end="\n\n")

# Apply a decorator to a standard library function
math.factorial = debug(math.factorial)

def approximate_e(terms=18):
    return f"e is about {sum(1 / math.factorial(n) for n in range(terms)):.6f}"

print(approximate_e(3), end='\n\n')

#using decorators to register functions
greeting_functions = dict()

def register(func):
    greeting_functions[func.__name__] = func
    return func
    #you don't need to write an inner function or use @functools.wraps
    #because you are returning the original function unmodified

@register
def say_hello(name):
    return f"Hello {name}"

@register
def be_awesome(name):
    return f"Yo {name}, together we are the awesomest!"

def randomly_greet(name):
    greeter, greeter_func = random.choice(list(greeting_functions.items()))
    print(f"Using {greeter!r}")
    return greeter_func(name)

print(greeting_functions, randomly_greet("Peter Parker"), sep="\n")

#nesting decorators
@debug
@timer
def greet(name):
    print(f'Hello {name}')

greet('Eva')

print()

#order matters, notice the difference
@timer
@debug
def greet2(name):
    print(f'Hello {name}')

greet2('James')