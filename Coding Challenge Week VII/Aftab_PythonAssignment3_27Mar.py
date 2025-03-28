def largest_rectangle_area(heights):
    stack = []
    max_area = 0
    heights.append(0)
    for i, h in enumerate(heights):
        start = i
        while stack and stack[-1][1] > h:
            index, height = stack.pop()
            max_area = max(max_area, height * (i - index))
            start = index
        stack.append((start, h))
    return max_area

def maximal_rectangle(nums):
    if not nums or not nums[0]:
        return 0
    n = len(nums)
    m = len(nums[0])
    heights = [0] * m
    max_rectangle = 0
    for i in range(n):
        for j in range(m):
            heights[j] = heights[j] + 1 if nums[i][j] == "1" else 0
        max_rectangle = max(max_rectangle, largest_rectangle_area(heights))
    return max_rectangle

ar = [["1", "0", "1", "0", "0"], ["1", "0", "1", "1", "1"], ["1", "1", "1", "1", "1"], ["1", "0", "0", "1", "0"]]
result = maximal_rectangle(ar)
print(result)