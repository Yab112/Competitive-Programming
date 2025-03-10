class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        target = sum(nums) - x
        ans = float("inf")
        l = r = runningSum = 0
        numsLen = len(nums)

        while r < numsLen:
            runningSum += nums[r]
            while l <= r and (runningSum > target) :
                runningSum -= nums[l]
                l += 1
            if runningSum == target:
                ans = min(ans, numsLen - (r - l + 1))
            r += 1

        return ans if ans != float("inf") else -1