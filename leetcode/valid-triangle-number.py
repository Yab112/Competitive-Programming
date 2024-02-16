from typing import List
from bisect import bisect_left

class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        
        sorted_nums = sorted(n for n in nums if n > 0)
        
        count = 0
        for i in range(len(sorted_nums) - 2):
            for j in range(i + 1, len(sorted_nums) - 1):
                
                k = bisect_left(sorted_nums, sorted_nums[i] + sorted_nums[j])
                
                count += k - j - 1
        
        return count
