
from collections import defaultdict
from typing import List

class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        res = len(nums)
        k = sum(nums) % p  
        
        if k == 0:
            return 0
        prextrm = 0
        prev_sum = {0: -1} 
        for i, num in enumerate(nums):
            prextrm  = (prextrm  + num) % p
            remainder = (prextrm - k )% p
            if remainder in prev_sum:
                res = min(res, i - prev_sum[remainder])
            prev_sum[prextrm] = i
        
        return res if res < len(nums) else -1
