class Solution:
    def maxArea(self, height: List[int]) -> int:
        first,last=0,len(height)-1
        max_area=0
        while first < last:
            size=(last -first)
            min_height=min(height[first], height[last])
            max_area=max(max_area,min_height*size)
            if height[last] < height[first]:
                last-=1
            else:
                first+=1
        return max_area
                