class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        pre_sum = [0] * len(nums)
        res = [0] * len(nums)
        pre_sum[0] = nums[0]
        for i in range(1,len(nums)):
            pre_sum[i] = pre_sum[i - 1] + nums[i]
        for i,num in enumerate(nums):
            
            if i - 1 < 0:
                res[i] = (num * i) + (pre_sum[-1] - pre_sum[i]) - (num*(len(nums) - i -1))
            elif i == len(nums) - 1:
                res[i] = (num * i) - pre_sum[i - 1] - (num*( len(nums)- i -1))
            else:
                res[i] = (num * i) - pre_sum[i - 1] + (pre_sum[-1] - pre_sum[i]) - (num*(len(nums) - i -1))
        return res
                    