from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        def l_r_max(nums):
            res = [0] * len(nums)
            num = nums[0]
            for i in range(1,len(nums)):
                res[i] = num
                num = max(num,nums[i])
            return res  
        l_max = l_r_max(height)
        r_max = l_r_max(height[::-1])[::-1]
        return sum([min(l_max[i],r_max[i]) - height[i] for i in range(len(height)) if min(l_max[i],r_max[i]) - height[i] >= 0])
        