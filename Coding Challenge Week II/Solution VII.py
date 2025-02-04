def rotate(arr):
    n = len(arr)
    for i in range(n):
        for j in range(i + 1, n):
            arr[i][j], arr[j][i] = arr[j][i], arr[i][j]
    for i in arr:
        i.reverse()
    return arr


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
rotate(matrix)
print(matrix)