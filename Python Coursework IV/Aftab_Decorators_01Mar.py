import time

def uppercase_decorators(func):
    def wrapper(args):
        result = func(args)
        return f"HELLO {result.upper()}"
    return wrapper

def timing_decorator(func):
    def wrapper(name):
        start = time.time()
        func(name)
        end = time.time()
        return f"{func.__name__} function ran in {end-start}"
    return wrapper

def say_hello(name):
    print(f"Hello {name}")
    return name

greet = uppercase_decorators(say_hello)
print(greet("Md Aftab Uddin"))
print()

timed_greet = timing_decorator(say_hello)
print(timed_greet("Md Aftab Uddin"))
print()


def logging_decorator(func):
    def wrapper(*args):
        result = func(*args)
        print(f"Calling {func.__name__} with arguments {args}. Result: {result}")
        return result
    return wrapper

class Math:
    @logging_decorator
    def add(self, a, b):
        return a+b

    @logging_decorator
    def subtract(self, a, b):
        return a-b

obj = Math()
print(obj.add(3, 5))
print(obj.subtract(10, 4))