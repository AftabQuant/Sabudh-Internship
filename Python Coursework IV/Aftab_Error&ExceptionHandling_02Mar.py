def divide_number(a, b):
    try:
        result = a/b
        return result
    except ZeroDivisionError:
        return f"Not divisible by 0..."

number1 = int(input("Enter 1st number: "))
number2 = int(input("Enter 2nd number: "))

print(divide_number(number1, number2))

class NegativeNumberError(Exception):
    pass

def check_number(num):
    if num<0:
        raise NegativeNumberError("Negative numbers are not allowed.")
    else: print("valid number:", num)

try :
    n = int(input("Enter a number: "))
    check_number(n)
except NegativeNumberError as e:
    print("Error", e)
finally :
    print("Program execution completed...")