def threeSum(num) :
    res = []
    for i in range(0, len(num)) :
        for j in range(i+1, len(num)) :
            for k in range(j+1, len(num)) :
                if num[i]+num[j]+num[k] == 0:
                    triplet = sorted([num[i], num[j], num[k]])
                    if triplet not in res : res.append(triplet)
    return res

nums1 = [-1, 0, 1, 2, -1, -4]
nums2 = [0,1,1]
nums3 =  [0,0,0]
print(threeSum(nums1))
print(threeSum(nums2))
print(threeSum(nums3))
