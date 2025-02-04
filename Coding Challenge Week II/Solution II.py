def rearrange_array(nums):
    n = len(nums)
    j=0
    for i in range(n):
        if nums[i] < 0:
            val = nums[i]
            k = i
            while k > j:
                nums[k] = nums[k - 1]
                k -= 1
            nums[j] = val
            j += 1
    return nums


arr = [-12, 11, -13, -5, 6, -7, 5, -3, -6]
print(rearrange_array(arr))

arr2 = [-12, 11, 13, -5, 6, -7, 5, -3, 8]
print(rearrange_array(arr2))

