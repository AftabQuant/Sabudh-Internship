class Node:
    def __init__(self, val, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def clone_graph(self, node: 'Node') -> 'Node':
        if not node:
            return None
        visited = {}
        def dfs(n):
            if n in visited:
                return visited[n]
            clone = Node(n.val)
            visited[n] = clone
            for neighbor in n.neighbors:
                clone.neighbors.append(dfs(neighbor))
            return clone
        return dfs(node)


node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)

node1.neighbors = [node2, node4]
node2.neighbors = [node1, node3]
node3.neighbors = [node2, node4]
node4.neighbors = [node1, node3]

# Clone the graph
solution = Solution()
cloned_node = solution.clone_graph(node1)

