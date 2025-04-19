class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def is_one_child(root):
    if root.left is None and root.right is None:
        return False
    if root.left is None or root.right is None:
        return True
    return is_one_child(root.left) and is_one_child(root.right)

if __name__ == "__main__":
    a = Node(20)
    b = Node(10)
    c = Node(11)
    d = Node(13)
    e = Node(12)

    a.left = b
    b.right = c
    c.right = d
    d.left = e

    print(is_one_child(a))