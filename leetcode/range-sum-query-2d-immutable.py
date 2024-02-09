class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        r = len(self.matrix)
        c = len(self.matrix[0])
        self.pref_sum = [[0 for i in range(c )] for j in range(r )]
        
        
        self.pref_sum[0][0] = self.matrix[0][0]
        
        
        for i in range(1,c):
            self.pref_sum[0][i] = self.pref_sum[0][i-1] + self.matrix[0][i]
            
        for i in range(1,r):
            self.pref_sum[i][0] = self.pref_sum[i - 1][0] + self.matrix[i][0]
        
        for i in range(1,r):
            for j in range(1,c):
                self.pref_sum[i][j] = self.pref_sum[i][j - 1] + self.pref_sum[i - 1][j] - self.pref_sum[i - 1][j - 1] + self.matrix[i][j]
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        temp1 = 0
        temp2 = 0
        temp3 = 0
        ans = 0
        if row1 - 1 >=  0:
            temp1 = self.pref_sum[row1-1][col2]
        if col1- 1 >= 0:
            temp2 = self.pref_sum[row2][col1 -1]
        if col1 - 1 >= 0 and row1 - 1 >= 0:
            temp3 = self.pref_sum[row1 - 1][col1 -1]
        ans = self.pref_sum[row2][col2] - temp1- temp2 + temp3
        return ans