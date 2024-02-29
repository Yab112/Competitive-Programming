class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        row_max = [max(i) for i in grid]
        col_max = []
        for i in range(len(grid[0])):
            val = 0
            for j in range(len(grid)):
                val =max(val,grid[j][i])

            col_max.append(val)
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                res += abs(grid[i][j] - min(col_max[j],row_max[i]))
        return res

