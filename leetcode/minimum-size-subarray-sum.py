class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        j = 0
        minim = len(nums)
        temp = 0
        flag = False
        for i in range(len(nums)):
            temp += nums[i]
            while temp >= target:
                flag = True
                minim = min(minim,i - j + 1)
                temp -= nums[j]
                j += 1
        return minim if flag  else 0