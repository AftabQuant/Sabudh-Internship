
def count_subsequence(s, t) :
    if len(s)>= len(t) and s.__contains__(t) : return len(t)
    elif len(s) < len(t) and t.__contains__(s) : return len(s)
    else: return 0


print(f"Common subsequence length of two strings is : {count_subsequence("abcde", "abc")}")
print(f"Common subsequence length of two strings is : {count_subsequence("abc", "abc")}")
print(f"Common subsequence length of two strings is : {count_subsequence("abc", "def")}")