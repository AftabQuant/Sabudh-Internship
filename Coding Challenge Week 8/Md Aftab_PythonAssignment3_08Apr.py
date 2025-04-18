def can_jump_end(nums):
    n = len(nums)
    reachable = [False] * n
    reachable[0] = True
    for i in range(n):
        if reachable[i]:
            for jump in range(1, nums[i] + 1):
                if i + jump < n:
                    reachable[i + jump] = True
    return reachable[-1]

print(can_jump_end([2, 3, 1, 1, 4]))
print(can_jump_end([3, 2, 1, 0, 4]))

