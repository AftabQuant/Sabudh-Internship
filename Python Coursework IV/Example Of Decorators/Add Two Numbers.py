def my_decorators(func):
    def wrapper(*args):
        print("Before function call...")
        print(func(*args))
        print("After function call...")
    return wrapper

@my_decorators
def add_numbers(a, b):
    return a+b

add_numbers(4,5)
print(add_numbers.__name__)