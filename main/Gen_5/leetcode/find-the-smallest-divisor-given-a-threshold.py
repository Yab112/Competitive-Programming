class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        l = 1
        r = max(nums)
        while l <= r:
            mid = l + (r - l)//2
            if self.simulate_effect(nums,mid,threshold):
                r = mid - 1
            else:
                l = mid + 1
        return l
    def simulate_effect(self,nums,mid,threshold):
        res = 0
        for i in nums:
            res += ceil(i / mid)
        return res <= threshold
