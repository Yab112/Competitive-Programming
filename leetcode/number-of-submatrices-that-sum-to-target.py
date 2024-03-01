class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        rows ,cols = len(matrix),len(matrix[0])
        res = 0
        cum_sum = [[0] * (cols + 1) for _ in range(rows + 1)]
        for r in range(rows):
            for c in range(cols):
                cum_sum[r+1][c+1] = cum_sum[r+1][c] + cum_sum[r][c+1] - cum_sum[r][c] + matrix[r][c]

        for r1 in range(1,rows + 1):
            for r2 in range(r1,rows + 1):
                prev_count = {0:1}
                runni_sum = 0
                for c in range(1,cols + 1):
                    runni_sum = cum_sum[r2][c] - cum_sum[r1 - 1][c]
                    res += prev_count.get(runni_sum - target,0)
                    prev_count[runni_sum] = prev_count.get(runni_sum,0) + 1
        return res 
        
