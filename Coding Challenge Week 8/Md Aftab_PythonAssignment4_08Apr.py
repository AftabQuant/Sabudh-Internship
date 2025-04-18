def manage_intervals(intervals):
    if not intervals:
        return []
    intervals.sort(key=lambda x: x[0])
    merged = [intervals[0]]
    for i in range(1, len(intervals)):
        prev = merged[-1]
        curr = intervals[i]
        if curr[0] <= prev[1]:
            prev[1] = max(prev[1], curr[1])
        else:
            merged.append(curr)
    return merged

print(manage_intervals([[1, 3], [2, 6], [8, 10], [15, 18]]))
print(manage_intervals([[1, 4], [4, 5]]))
