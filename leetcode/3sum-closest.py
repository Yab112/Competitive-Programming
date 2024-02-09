class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        if len(nums) < 3 :
            return 0
        m = sum(nums[:3])
        for i,val in enumerate(nums):
            l = i + 1
            r = len(nums) - 1
            while l < r:
                sum_nums = val + nums[l] + nums[r]
                if sum_nums == target:
                    return sum_nums
                elif abs(sum_nums - target) < abs(m - target):
                    m = sum_nums
                elif sum_nums > target:
                    r -= 1
                else:
                    l += 1
        return m
           
                