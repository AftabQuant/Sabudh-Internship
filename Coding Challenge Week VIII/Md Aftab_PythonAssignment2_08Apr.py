def simplify_path(path):
    stack = []
    parts = path.split('/')
    for part in parts:
        if part == '' or part == '.':
            continue
        elif part == '..':
            if stack:
                stack.pop()
        else:
            stack.append(part)

    result = '/' + '/'.join(stack)
    return result

print(simplify_path("/home/"))
print(simplify_path("/home/foo/"))
print(simplify_path("/home/user/Documents/../Pictures"))
print(simplify_path("/../"))
print(simplify_path("/.../a/../b/c/../d/./"))
