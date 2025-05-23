def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def say_hello():
    print("Hello...")

@my_decorator
def say_nothing():
    print("Nothing...")

say_hello()
print()
say_nothing()