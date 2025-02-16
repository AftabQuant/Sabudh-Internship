def  max_length(arr, k):
    prefix_sum = 0
    index = {}
    max_length = 0
    for i in range(len(arr)):
        prefix_sum += arr[i]
        if prefix_sum == k:
            max_length = i + 1
        if prefix_sum - k in index:
            max_length = max(max_length, i - index[prefix_sum - k])
        if prefix_sum not in index:
            index[prefix_sum] = i
    return max_length

nums =  [10, 5, 2, 7, 1, -10]
k = 15
print(max_length(nums, k))