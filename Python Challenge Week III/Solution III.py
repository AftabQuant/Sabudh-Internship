def sum_zero_triplets(nums):
    nums.sort()
    n = len(nums)
    result = []
    for i in range(n - 2) :
        if i > 0 and nums[i] == nums[i - 1] :
            continue
        left = i + 1
        right = n - 1
        while left < right:
            current_sum = nums[i] + nums[left] + nums[right]
            if current_sum == 0:
                result.append([nums[i], nums[left], nums[right]])
                left += 1
                right -= 1
                while left < right and nums[left] == nums[left - 1]:
                    left += 1
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1
            elif current_sum < 0:
                left += 1
            else:
                right -= 1
    return result

arr1 = [-1, 0, 1, 2, -1, -4]
print("Triplets summing to zero:", sum_zero_triplets(arr1))

arr2 = [0, 1, 1]
print("Triplets summing to zero:", sum_zero_triplets(arr2))

arr3 = [0, 0, 0]
print("Triplets summing to zero:", sum_zero_triplets(arr3))

arr4 = [-2,0,0,2,2]
print("Triplets summing to zero:", sum_zero_triplets(arr4))