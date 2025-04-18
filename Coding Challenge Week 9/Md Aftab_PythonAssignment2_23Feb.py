
def longest_consecutive_elements(nums) :
    my_set = set(nums)
    maxLength = 0
    for ele in nums :
        if ele-1 not in my_set:
            curr = ele
            length = 1
        while curr+1 in my_set:
            curr += 1
            length += 1
        maxLength = max(length, maxLength)

    return maxLength

num = [100, 4, 200, 1, 3, 2]
print(longest_consecutive_elements(num))