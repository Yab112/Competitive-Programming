class Solution:
    def rob(self, nums: List[int]) -> int:  
        if not nums:    
            return 0  
        if len(nums) == 1:  # Handle edge case of a single house  
            return nums[0]  
        
        prev1, prev2 = 0, 0  
        for num in nums:  
            current = max(prev2 + num, prev1)  
            prev2 = prev1  
            prev1 = current  
        
        return prev1  





                
            