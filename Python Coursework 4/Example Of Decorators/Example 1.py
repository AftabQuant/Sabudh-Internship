import time

def timer(func):
    def wrapper(*args):
        st = time.time()
        result = func(*args)
        end = time.time()
        print(f"{func.__name__} ran in {end-st} time")
        return result
    return wrapper

@timer
def example(n):
    time.sleep(n)

example(2)