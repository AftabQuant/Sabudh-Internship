def min_difference(nums, stu) :
    n = len(nums)
    nums.sort()

    min_diff = float('inf')
    for i in range(n - stu + 1):
        diff = nums[i + stu - 1] - nums[i]
        min_diff = min(diff, min_diff)
    return min_diff

arr = [7, 3, 2, 4, 9, 12, 56]
m = 3
print("Minimum Difference is:", min_difference(arr, m))