class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points = sorted(points,key=lambda x: x[1])
        start = points[0][1]
        arrow = 1
        for i in range(1,len(points)):
            if  points[i][0] <= start:
                continue
            else:
                arrow += 1
                start = points[i][1] 
        return arrow 

        
