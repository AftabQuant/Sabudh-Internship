def search_element_matrix(nums, target):
    m, n = len(nums), len(nums[0])
    row, col = 0, n - 1
    while row < m and col >= 0:
        if nums[row][col] == target:
            return True
        elif nums[row][col] > target:
            col -= 1
        else:
            row += 1
    return False

a = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
target1 = 5

b = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
target2 = 20

print(search_element_matrix(a, target1))
print(search_element_matrix(b, target2))

