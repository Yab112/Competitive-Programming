class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        pref = list(accumulate(nums))
        res = 0
        for i in range(len(nums)):
            res = max(res,ceil(pref[i]/(i + 1)))
        
        return res 