class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        dic = Counter(nums)
        return [i for i ,j in dic.items() if j >= 2]
