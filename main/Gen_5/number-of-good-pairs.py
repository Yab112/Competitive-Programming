from collections import Counter
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        freq = Counter(nums)
        count = list(freq.values())
        print(count)
        sum = 0
        for i in count:
            goodPairs = (i * (i-1))//2
            sum+=goodPairs
        return sum