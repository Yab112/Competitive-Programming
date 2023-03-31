class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        n = len(piles)
        sum_ = 0
        for i in range(n//3,n,2):
            sum_ += piles[i]
        return sum_
            