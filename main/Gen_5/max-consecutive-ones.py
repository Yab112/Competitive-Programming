class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        l_pointer = 0
        r_pointer = 0
        max_window = 0
        while l_pointer <= r_pointer and r_pointer < len(nums):
            window_size = 0
            while  r_pointer < len(nums) and nums[r_pointer] == 1 :
                r_pointer += 1
            window_size += r_pointer  - l_pointer
            r_pointer += 1
            l_pointer = r_pointer
            
            if max_window < window_size:
                max_window = window_size
        return max_window 

        