class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        up_move = True
        row_length = len(mat)
        col_length = len(mat[0])
        row = col = 0
        flatten_array = []
        while row < row_length and col < col_length:
            if up_move:
                while row > 0 and col < col_length - 1:
                    flatten_array.append(mat[row][col]) 
                    row -= 1
                    col += 1
                flatten_array.append(mat[row][col])
                if col == col_length - 1:
                    row += 1
                else: 
                    col += 1
                up_move = False
            else:
                while row < row_length - 1 and col > 0: 
                    flatten_array.append(mat[row][col])
                    row += 1
                    col -= 1 
                flatten_array.append(mat[row][col])
                if row == row_length - 1:
                    col += 1
                else:
                    row += 1
                up_move = True

        return flatten_array