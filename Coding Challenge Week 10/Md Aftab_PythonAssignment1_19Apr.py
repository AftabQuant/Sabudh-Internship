class Node :
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def maximum_depth(root) :
    if root is None: return 0
    return 1 + max(maximum_depth(root.left), maximum_depth(root.right))

if __name__ == "__main__":
    a = Node(1)
    b = Node(2)
    c = Node(3)
    d = Node(4)
    e = Node(5)
    f = Node(6)
    g = Node(7)
    h = Node(8)
    i = Node(9)

    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.left = f
    c.right = g
    d.left = h
    d.right = i

    print(maximum_depth(a))