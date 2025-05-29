def smallest_missing_element(nums) :
    n = len(nums)
    res = [0] * 100

    for i in range(n) :
        res[nums[i]] += 1

    for i in range(len(res)) :
        if res[i] == 0 :
            return i

    return 0

nums1 = [0, 1, 2, 6, 9, 11, 15]
print(f"The smallest missing element is : {smallest_missing_element(nums1)}")

nums2 = [1, 2, 3, 4, 6, 9, 11, 15]
print(f"The smallest missing element is : {smallest_missing_element(nums2)}")
