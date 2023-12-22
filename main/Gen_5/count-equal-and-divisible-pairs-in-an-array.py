class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        no_good_pair = 0
        for i in range(len(nums)):
            for j in range(i + 1,len(nums)):
                if i < j and nums[i] == nums[j] and (i * j ) % k == 0:
                    no_good_pair += 1
        return no_good_pair
