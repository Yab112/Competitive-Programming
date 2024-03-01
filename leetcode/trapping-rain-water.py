from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        
        l = 0
        r = len(height) - 1
        l_max = height[l]
        r_max = height[r]
        res = 0
        
        while l < r:
            if l_max < r_max:
                if l_max - height[l] > 0:
                    res += (l_max - height[l])
                l += 1
                l_max = max(l_max,height[l])
            else:
                if r_max - height[r] > 0:
                    res += (r_max - height[r])
                r -= 1
                r_max = max(height[r],r_max)
        
        return res
