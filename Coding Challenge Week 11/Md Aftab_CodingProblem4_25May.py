from typing import List

class Solution:
    def pacific_atlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights or not heights[0]:
            return []
        rows, cols = len(heights), len(heights[0])
        pacific_reach = [[False] * cols for _ in range(rows)]
        atlantic_reach = [[False] * cols for _ in range(rows)]
        def dfs(r, c, visited, prev_height):
            if (r < 0 or r >= rows or c < 0 or c >= cols or
                visited[r][c] or heights[r][c] < prev_height):
                return
            visited[r][c] = True
            directions = [(1,0), (-1,0), (0,1), (0,-1)]
            for dr, dc in directions:
                dfs(r + dr, c + dc, visited, heights[r][c])
        for i in range(rows):
            dfs(i, 0, pacific_reach, heights[i][0])
            dfs(i, cols - 1, atlantic_reach, heights[i][cols - 1])
        for j in range(cols):
            dfs(0, j, pacific_reach, heights[0][j])
            dfs(rows - 1, j, atlantic_reach, heights[rows - 1][j])
        result = []
        for r in range(rows):
            for c in range(cols):
                if pacific_reach[r][c] and atlantic_reach[r][c]:
                    result.append([r, c])
        return result

heights = [
    [1,2,2,3,5],
    [3,2,3,4,4],
    [2,4,5,3,1],
    [6,7,1,4,5],
    [5,1,1,2,4]
]

sol = Solution()
print(sol.pacific_atlantic(heights))
