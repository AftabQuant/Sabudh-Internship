def count_consistent_strings(allow, words):
    allowed_set = set(allow)
    count = 0
    for word in words:
        flag = True
        for char in word:
            if char not in allowed_set:
                flag = False
                break
        if flag:
            count += 1
    return count