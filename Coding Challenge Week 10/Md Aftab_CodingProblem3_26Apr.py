class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def calculate_sum(root):
    if root is None: return 0
    return root.val + calculate_sum(root.left) + calculate_sum(root.right)

def is_equal_to_sum(root, target_sum):
    if root is None: return False
    subtree_sum = calculate_sum(root)
    if subtree_sum == target_sum: return True
    return is_equal_to_sum(root.left, target_sum) or is_equal_to_sum(root.right, target_sum)

if __name__ == "__main__":
    a = Node(1)
    b = Node(3)
    c = Node(6)
    d = Node(5)
    e = Node(9)
    f = Node(8)

    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.left = f
    if is_equal_to_sum(a, 17) :
        print("Yes...")
    else :
        print("No...")