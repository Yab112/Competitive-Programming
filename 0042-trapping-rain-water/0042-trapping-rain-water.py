class Solution:    
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        
        n = len(height)
        
        # Calculate max to the left
        max_left = [0] * n
        max_left[0] = height[0]
        for i in range(1, n):
            max_left[i] = max(height[i], max_left[i - 1])
        
        # Calculate max to the right
        max_right = [0] * n
        max_right[-1] = height[-1]
        for i in range(n - 2, -1, -1):
            max_right[i] = max(height[i], max_right[i + 1])
        
        # Calculate water trapped
        water = 0
        for i in range(n):
            trapped = min(max_left[i], max_right[i]) - height[i]
            if trapped > 0:
                water += trapped
        
        return water
