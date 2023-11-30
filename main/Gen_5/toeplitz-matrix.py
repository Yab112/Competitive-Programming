class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if not all(matrix[i][j] == matrix[i + k][j + k] for k in range(1, min(len(matrix) - i, len(matrix[0]) - j))):
                    return False
        return True