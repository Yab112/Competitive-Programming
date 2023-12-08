from typing import List

class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        if len(nums) <= 2:
            return True
        
        modified = False  
        for i in range(1, len(nums)):
            if nums[i] < nums[i - 1]:
                if modified:
                    return False
                if i >= 2 and nums[i] < nums[i - 2]:
                    nums[i] = nums[i - 1]
                else:
                    nums[i - 1] = nums[i]
                
                modified = True
        
        return True