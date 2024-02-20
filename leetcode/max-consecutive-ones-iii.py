class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        zeros = 0 
        res =l = 0 
        for i,num in enumerate(nums):
            if num == 0:
                zeros += 1
            while zeros > k:
                if nums[l] == 0:
                    zeros -= 1
                l += 1
            res = max(res,i - l + 1 )
        return max(res,i - l + 1 ) 

