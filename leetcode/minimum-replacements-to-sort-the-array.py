class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        len_ = len(nums)
        prev_value = nums[-1]
        
        operation = 0
        
        for i in range(len(nums)-2,-1,-1):
            if nums[i] > prev_value:
                
                k = (nums[i] + prev_value - 1) // prev_value
                prev_value = nums[i]//k
                operation += k - 1
            else:
                prev_value = nums[i]
        return operation