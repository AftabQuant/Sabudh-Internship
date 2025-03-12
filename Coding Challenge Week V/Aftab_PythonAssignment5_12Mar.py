class SparseVector:
    def __init__(self, nums):
        self.nums = nums

    def dotProduct(self, vec):
        result = 0
        for i in range(len(self.nums)):
            result += self.nums[i] * vec.nums[i]
        return result

a = [1, 0, 0, 2, 3]
b = [0, 3, 0, 4, 0]
v1 = SparseVector(a);
v2 = SparseVector(b);
print(v1.dotProduct(v2))