class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count=0       
        for first in range(len(nums)):
            for last in range(first+1,len(nums)):
                if nums[first]==nums[last]:
                    count+=1
        return count 
            