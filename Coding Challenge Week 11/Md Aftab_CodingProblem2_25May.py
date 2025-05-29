from collections import deque, defaultdict

class Solution:
    def can_finish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        graph = defaultdict(list)
        in_degree = [0] * numCourses
        for dest, src in prerequisites:
            graph[src].append(dest)
            in_degree[dest] += 1
        queue = deque([i for i in range(numCourses) if in_degree[i] == 0])
        completed_courses = 0
        while queue:
            course = queue.popleft()
            completed_courses += 1
            for neighbor in graph[course]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
        return completed_courses == numCourses

sol = Solution()
print(sol.can_finish(2, [[1, 0]]))
print(sol.can_finish(2, [[1, 0], [0, 1]]))

