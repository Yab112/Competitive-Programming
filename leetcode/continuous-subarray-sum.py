class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        dic = {0:-1}
        res = 0
        for i in range(len(nums)):
            res += nums[i]
            res %= k
            if res % k not in dic:
                dic[res] = i
            elif i - dic[res] >= 2:
                return True
        return False

        