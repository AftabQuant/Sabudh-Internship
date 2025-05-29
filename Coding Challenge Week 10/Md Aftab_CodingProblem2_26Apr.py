class Node :
    def __init__(self, val) :
        self.val = val
        self.left = None
        self.right = None

def is_same_tree(p, q) :
    if p is None and q is None: return True
    if p is None or q is None : return False
    if p.val != q.val : return False
    if not is_same_tree(p.left, q.left) : return False
    if not is_same_tree(p.right, q.right) : return False
    return True

if __name__ == "__main__":
    a = Node(1)
    b = Node(2)
    c = Node(3)
    d = Node(4)

    p = Node(1)
    q = Node(2)
    r = Node(3)
    s = Node(4)

    a.left = b
    a.right = c
    b.left = d

    p.left = q
    p.right = r
    q.left = s

    if is_same_tree(a, p) :
        print("Both trees are identical...")
    else :
        print("Trees are not identical...")