def next_permutation(nums):
    n = len(nums)
    i = n - 2
    lo = i + 1
    hi = n - 1
    while lo < hi:
        nums[lo], nums[hi] = nums[hi], nums[lo]
        lo += 1
        hi -= 1

nums1 = [1, 2, 3]
next_permutation(nums1)
print(nums1)

nums2 = [3, 2, 1]
next_permutation(nums2)
print(nums2)
