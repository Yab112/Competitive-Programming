class Solution:
    def canJump(self, nums: List[int]) -> bool:
        a = len(nums) - 1
         
        for i in range(len(nums) -2,-1,-1):
            dif = a - i
            if dif <= nums[i]:
                a = i
        if a == 0:
            return True 
        else:
            return False

    
            