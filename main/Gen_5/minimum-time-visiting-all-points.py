from typing import List

class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        minimum_time = 0

        for i in range(len(points) - 1):
            x_diff = abs(points[i][0] - points[i+1][0])
            y_diff = abs(points[i][1] - points[i+1][1])
            
         
            diagonal_moves = min(x_diff, y_diff)
            
           
            remaining_moves = abs(x_diff - y_diff)
            
            minimum_time += diagonal_moves + remaining_moves

        return minimum_time
