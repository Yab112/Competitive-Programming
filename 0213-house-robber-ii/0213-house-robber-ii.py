class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) ==0:return 0
        if len(nums) ==1:return nums[0]
        def rob(nums:list)->int:
            lft2,lft1 = 0,0
            for num in nums:
                crt = max(lft2 + num,lft1)
                lft2 = lft1
                lft1 = crt
            return lft1
        return max(rob(nums[:-1]),rob(nums[1:]))
    
