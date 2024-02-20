class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        l  = 0
        zero = 0
        res = 0
        for i,num in enumerate(nums):
            if num == 0:
                zero += 1
            while zero > 1:
                if nums[l] == 0:
                    zero-=1
                l += 1
            res = max(res,i - l + 1)
        return max(res,i - l + 1) - 1