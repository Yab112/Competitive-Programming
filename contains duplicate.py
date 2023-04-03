class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        checker = {}
        for i in nums:
            if i not in checker:
                checker[index(i)]= i
            else:
                return True
        return False
