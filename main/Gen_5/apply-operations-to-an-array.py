class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            if i + 1 < len(nums) and nums[i] == nums[i + 1] :
                nums[i] = 2 * nums[i]
                nums[i+1] = 0
        l , r = 0,1
        while l <= r and r < len(nums):
            if nums[l] != 0:
                l += 1
                r = l
            elif nums[l] == 0 and nums[r] != 0:
                temp = nums[l]
                nums[l] = nums[r]
                nums[r] = temp
                l += 1
                r += 1
            else:
                r += 1
        return nums
            
                