# https://leetcode.com/problems/difference-between-ones-and-zeros-in-row-and-column/

class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        m, n = len(grid), len(grid[0])

        diff = [[0] * n for _ in range(m)]

        ones_row = [0] * m
        zeros_row = [0] * m
        ones_col = [0] * n
        zeros_col = [0] * n

        for i in range(m):
            ones_row[i] = sum(grid[i])
            zeros_row[i] = n - ones_row[i]

        for j in range(n):
            ones_col[j] = sum(grid[row][j] for row in range(m))
            zeros_col[j] = m - ones_col[j]

        for i in range(m):
            for j in range(n):
                diff[i][j] = ones_row[i] + ones_col[j] - zeros_row[i] - zeros_col[j]

        return diff
