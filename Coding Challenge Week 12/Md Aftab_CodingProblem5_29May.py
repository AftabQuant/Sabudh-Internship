def count_ways(n):
    if n == 0 or n == 1:
        return 1
    prev, curr = 1, 1
    for _ in range(2, n + 1):
        prev, curr = curr, prev + curr
    return curr

print("Input: n = 1")
print("Output:", count_ways(1))

print("\nInput: n = 2")
print("Output:", count_ways(2))

print("\nInput: n = 4")
print("Output:", count_ways(4))
