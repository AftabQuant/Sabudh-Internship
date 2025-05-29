def length_of_lis(arr):
    n = len(arr)
    dp = [1] * n
    for i in range(n):
        for j in range(i):
            if arr[i] > arr[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)

nums = [10, 9, 2, 5, 3, 7, 101, 18]
print(f"Length of the longest strictly increasing subsequence:{length_of_lis(nums)}")

nums2 = [7,7,7,7,7,7,7]
print(f"Length of the longest strictly increasing subsequence:{length_of_lis(nums2)}")

