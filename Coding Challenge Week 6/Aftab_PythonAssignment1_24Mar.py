def product_except_self(nums) :
    result = [1] * len(nums)
    pre = 1
    for i in range(len(nums)):
        result[i] = pre
        pre *= nums[i]
    suf = 1
    for i in range(len(nums)-1, -1, -1):
        result[i] *= suf
        suf*= nums[i]
    return result

a = [1,2,3,4]
print(product_except_self(a))