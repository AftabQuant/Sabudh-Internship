def next_smaller(arr):
    n = len(arr)
    nse = [n] * n
    stack = []
    for i in range(n - 1, -1, -1):
        while stack and arr[stack[-1]] >= arr[i]:
            stack.pop()
        nse[i] = stack[-1] if stack else n
        stack.append(i)
    return nse

def prev_smaller(arr):
    n = len(arr)
    pse = [-1] * n
    stack = []
    for i in range(n):
        while stack and arr[stack[-1]] >= arr[i]:
            stack.pop()
        pse[i] = stack[-1] if stack else -1
        stack.append(i)
    return pse

def largest_rectangle_area(heights):
    n = len(heights)
    nse = next_smaller(heights)
    pse = prev_smaller(heights)
    max_area = 0
    for i in range(n):
        height = heights[i] * (nse[i] - pse[i] - 1)
        max_area = max(max_area, height)
    return max_area

a =  [0,1,0,2,1,0,1,3,2,1,2,1]
print(largest_rectangle_area(a))
