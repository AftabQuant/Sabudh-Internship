class Node:
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None

def is_sum_tree(root):
    return is_sum_tree_util(root)[0]

def is_sum_tree_util(root):
    if root is None:
        return True, 0

    if root.left is None and root.right is None:
        return True, root.data

    left_result, left_sum = is_sum_tree_util(root.left)
    right_result, right_sum = is_sum_tree_util(root.right)

    is_current_node_sum_tree = (root.data == left_sum + right_sum)

    return (left_result and right_result and is_current_node_sum_tree), (left_sum + right_sum)

if __name__ == "__main__":
    a = Node(26)
    b = Node(10)
    c = Node(3)
    d = Node(4)
    e = Node(6)
    f = Node(3)

    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.right = f

    result = is_sum_tree(a)
    if result:
        print("The given tree is a SumTree")
    else:
        print("The given tree is not a SumTree")