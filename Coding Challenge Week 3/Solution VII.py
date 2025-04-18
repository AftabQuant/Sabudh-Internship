def count_successful_pairs(spells, potions, success):
    n = len(spells)
    m = len(potions)
    pairs = [0] * n
    potions.sort()
    for i in range(n):
        count = 0
        left = 0
        right = m - 1
        while left <= right:
            mid = (left + right) // 2
            if spells[i] * potions[mid] >= success:
                count = m - mid
                right = mid - 1
            else:
                left = mid + 1
        pairs[i] = count
    return pairs

spells1 = [5, 1, 3]
potions1 = [1, 2, 3, 4, 5]
success1 = 7
print(count_successful_pairs(spells1, potions1, success1))

spells2 = [3, 1, 2]
potions2 = [8, 5, 8]
success2 = 16
print(count_successful_pairs(spells2, potions2, success2))

spells3 = [2, 1, 4]
potions3 = [1, 2, 3, 4, 5, 6, 7]
success3 = 10
print(count_successful_pairs(spells3, potions3, success3))

spells4 = [1,2,3,4,5]
potions4 = [1,2,3,4,5]
success4 = 6
print(count_successful_pairs(spells4, potions4, success4))