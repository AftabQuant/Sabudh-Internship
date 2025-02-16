def max_product_triplet(nums):
    nums.sort()
    n = len(nums)
    opt1 = (nums[n - 1], nums[n - 2], nums[n - 3])
    opt2 = (nums[0], nums[1], nums[n - 1])
    return max(opt1, opt2, key=lambda x: x[0] * x[1] * x[2])

arr1 = [-4, 1, -8, 9, 6]
print("The triplet having the maximum product is", max_product_triplet(arr1))

arr2 = [1, 7, 2, -2, 5]
print("The triplet having the maximum product is", max_product_triplet(arr2))