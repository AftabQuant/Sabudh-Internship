def my_decorators(func):
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        print(f"{func.__name__}, {args}")
    return wrapper

@my_decorators
def func1(greet, greeting="hello"):
     print(f"{greeting}, {greet}")

func1("Aftab")

