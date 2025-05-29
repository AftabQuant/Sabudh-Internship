def generate_strings(char_set, k):
    def generate_recursive(prefix, k):
        if k == 0:
            print(prefix)
            return
        for char in char_set:
            generate_recursive(prefix + char, k - 1)
    generate_recursive('', k)


print("Output for set = ['a', 'b'], k = 3:")
generate_strings(['a', 'b'], 3)

print("\nOutput for set = ['a', 'b', 'c', 'd'], k = 1:")
generate_strings(['a', 'b', 'c', 'd'], 1)
