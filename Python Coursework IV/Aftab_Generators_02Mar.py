def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a+b

fibo = fibonacci(10)
for num in fibo:
    print(num, end=" ")
print()

def is_prime(n):
    for i in range(2,n+1):
        flag = True
        for j in range(2,i):
            if i%j == 0:
                flag = False
                break
        if flag : yield i


for num in is_prime(100):
    print(num, end=" ")
print()

# def generate_words(string):
#     for word in string.split():  
#         yield word.strip(".,!?")

def unique_words_generator(words_list):
    seen = set()
    for word in words_list:
        word_lower = word.lower()
        if word_lower not in seen:
            seen.add(word_lower)
            yield word.strip(".,!?")

test_string = "The quick brown fox jumps over the lazy dog."
test_list = ["The", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"]
print("\nThe unique words are:")
for word in unique_words_generator(test_list):
    print(word, end=" ")

def generate_sublist(arr, n):
    for i in range(len(arr)-n+1):
        yield arr[i: i+n]

arr = [1,2,3,4,5,6,7,8,9]
for ele in generate_sublist(arr=arr, n=3):
    print(ele, end=" ")