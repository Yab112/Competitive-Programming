from copy import deepcopy
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        new_matrix = deepcopy(matrix)
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                matrix[i][j] = new_matrix[j][i]
        for i in range(len(matrix)):
            matrix[i] = matrix[i][::-1]
        """
        Do not return anything, modify matrix in-place instead.
        """
        