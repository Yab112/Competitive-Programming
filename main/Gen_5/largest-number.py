from typing import List

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        for num in range(len(nums)):
            nums[num] = str(nums[num])        
        def compare_them(n1,n2):
            if n1 + n2 > n2 + n1:
                return -1
            else:
                return 1
        new_num = sorted(nums,key=cmp_to_key(compare_them))
        return str(int("".join(new_num)))