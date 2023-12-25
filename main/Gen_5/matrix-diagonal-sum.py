class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        diagonal_one = sum([mat[row][col] for row,col in zip(range(len(mat)),range(len(mat[0])) ) if row == col])
        diagonal_two = 0
        i = 0
        j = len(mat[0]) - 1
        while i < len(mat) and j >= 0 :
            if i != j:
                diagonal_two += mat[i][j]
            i +=1 
            j -= 1
        return diagonal_one+diagonal_two 