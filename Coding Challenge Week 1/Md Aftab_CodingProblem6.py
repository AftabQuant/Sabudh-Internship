def convert_int(st) :
    roman_values = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }
    sum = 0
    prev = 0
    for char in reversed(st):
        curr = roman_values[char]
        if curr < prev:
            sum -= curr
        else:
            sum += curr

        prev = curr
    return sum

print(convert_int("III"))
print(convert_int("LVIII"))