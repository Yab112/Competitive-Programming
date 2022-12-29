class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        yo=[0]*len(nums)
        n = len(nums)
        for i in range(n):
            key = nums[i]
            for j in range(n):
                if nums[j] < key and nums[j] != key:
                    yo[i] += 1
        return yo