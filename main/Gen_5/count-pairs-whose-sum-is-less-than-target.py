class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        k = 0
        r = 1
        for i in range(len(nums)):
            r = i + 1
            while r < len(nums):
                if nums[r] + nums[i] < target:
                    k +=1 
                r += 1
        return k 