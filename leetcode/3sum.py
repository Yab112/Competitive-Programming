class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = set()
        for i,value in enumerate(nums):
            j = i+ 1
            k = len(nums) - 1
            while j < k:
                n_1 = nums[j]
                n_2 = nums[k]
                target = value + n_1 + n_2
                if target  == 0:
                    res.add((value,n_1,n_2))
                    j += 1
                    k -= 1
                elif target > 0:
                    k -= 1
                elif target < 0:
                    j += 1
        return res
                    
            