def largest_subarray_sum(arr):
    max_sum = arr[0]
    current_sum = arr[0]
    for i in range(1, len(arr)):
        current_sum = max(arr[i], current_sum + arr[i])
        max_sum = max(max_sum, current_sum)
    return max_sum

a = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(f"The largest sum is: {largest_subarray_sum(a)}")

b = [5,4,-1,7,8]
print(f"The largest sum is: {largest_subarray_sum(b)}")