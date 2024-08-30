class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        x_area = 0
        y_area = 0
        z_area = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] > 0:
                    x_area += 1
            z_area += max(grid[i])
        for idx in range(len(grid)):
            y_max = float('-inf')
            for i in range(len(grid)):
                if grid[i][idx] > y_max:
                    y_max = grid[i][idx]
            y_area += y_max
        return x_area + y_area + z_area