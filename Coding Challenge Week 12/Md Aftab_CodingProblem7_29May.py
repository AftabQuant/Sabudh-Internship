class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def pathSum(root, targetSum):
    result = []
    def dfs(node, current_path, current_sum):
        if not node:
            return
        current_path.append(node.val)
        current_sum += node.val
        if not node.left and not node.right and current_sum == targetSum:
            result.append(list(current_path))  # Make a copy of the path

        dfs(node.left, current_path, current_sum)
        dfs(node.right, current_path, current_sum)

        current_path.pop()
    dfs(root, [], 0)
    return result

if __name__ == "__main__" :
    # Construct the tree
    root = TreeNode(5)
    root.left = TreeNode(4)
    root.right = TreeNode(8)

    root.left.left = TreeNode(11)
    root.left.left.left = TreeNode(7)
    root.left.left.right = TreeNode(2)

    root.right.left = TreeNode(13)
    root.right.right = TreeNode(4)
    root.right.right.left = TreeNode(5)
    root.right.right.right = TreeNode(1)

    # Find paths that sum to 22
    target = 22
    paths = pathSum(root, target)

    # Print results
    print("Paths with sum", target, ":")
    for path in paths:
        print(path)

