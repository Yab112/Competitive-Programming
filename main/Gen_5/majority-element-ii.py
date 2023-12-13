class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
      num = collections.Counter(nums)
      more_than = [i for i, j in num.items() if j >= (len(nums)//3) + 1 ]
      return more_than
     