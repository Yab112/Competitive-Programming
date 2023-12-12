class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        return sum(range(min(nums),len(nums ) + 1)) - sum(nums)
            
        