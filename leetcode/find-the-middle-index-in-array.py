class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
      prefix_sum_f = [0] * len(nums)  
      prefix_sum_b = [0] * len(nums)  
      prefix_sum_f[0] = nums[0]
      prefix_sum_b[-1] = nums[-1]
      if len(nums) == 1:
          return 0
      for i in range(1,len(nums)):
          prefix_sum_f[i] = prefix_sum_f[i - 1] + nums[i]
      for i in range(len(nums) - 2,-1,-1):
          prefix_sum_b[i] = prefix_sum_b[i + 1] + nums[i]
      if prefix_sum_b[1] == 0:
            return 0
      for i in range(len(nums)):
          if prefix_sum_f[i] == prefix_sum_b[i]:
                return i
      if prefix_sum_f[-2] == 0:
           return len(nums) - 1
      return -1
      
      
     