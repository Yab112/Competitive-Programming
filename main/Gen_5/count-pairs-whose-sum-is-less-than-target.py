class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        nums.sort()
        l=k = 0
        r = len(nums) -1 
        while r > l:
            if nums[r] + nums[l] < target:
                k +=( r - l)
                l += 1
            else:
                r -= 1
        return k 