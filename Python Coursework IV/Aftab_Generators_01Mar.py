def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a+b

def is_prime(n):
    for i in range(2,n+1):
        flag = True
        for j in range(2,i):
            if i%j == 0:
                flag = False
                break
        if flag : yield i

def generate_word(string):

    
fibo = fibonacci(10)
for num in fibo:
    print(num, end=" ")
print()

for num in is_prime(100):
    print(num, end=" ")
print()

