def total_pair(nums, k):
    res = []
    for i in range(0, len(nums)):
        for j in range(i+1, len(nums)) :
            if nums[i]+nums[j] == k:
                res.append([nums[i], nums[j]])
    return len(res)

arr = [1,5,7,-1]
print(total_pair(arr,6))

arr1 = [1,5,7,-1,5]
print(total_pair(arr1,6))