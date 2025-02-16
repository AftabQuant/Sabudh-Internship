def trapped_water(arr):
    n = len(arr)
    left_max = [0] * n
    right_max = [0] * n
    water = 0
    left_max[0] = arr[0]
    for i in range(1, n):
        left_max[i] = max(arr[i], left_max[i - 1])
    right_max[n - 1] = arr[n - 1]
    for i in range(n - 2, -1, -1):
        right_max[i] = max(arr[i], right_max[i + 1])
    for i in range(n):
        water += max(0, min(left_max[i], right_max[i]) - arr[i])
    return water

arr1 = [0, 2, 0, 2, 0]
print(trapped_water(arr1))

arr2 = [4,2,0,3,2,5]
print(trapped_water(arr2))

arr3 = [0,1,0,2,1,0,1,3,2,1,2,1]
print(trapped_water(arr3))