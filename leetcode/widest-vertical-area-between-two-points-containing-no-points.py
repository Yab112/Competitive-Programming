class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
      mad_d = 0

      points.sort(key= lambda x: x[0]) 
      for i in range(1,len(points)):
          mad_d = max(mad_d,points[i][0] - points[i-1][0] )
      return mad_d