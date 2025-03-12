from collections import Counter

def unique_element(nums):
    freq_map = Counter(nums)
    res = [key for key, freq in freq_map.items() if freq==1]
    return res

ar = [1,2,1,3,2,5]
print(unique_element(ar))

br = [-1, 0]
print(unique_element(br))

cr = [0,1]
print(unique_element(cr))