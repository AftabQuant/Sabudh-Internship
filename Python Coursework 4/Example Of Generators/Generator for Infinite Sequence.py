def infinite_numbers():
    number = 0
    while True:
        yield number
        number += 1

gen = infinite_numbers()
print(next(gen))
print(next(gen))
print(next(gen))