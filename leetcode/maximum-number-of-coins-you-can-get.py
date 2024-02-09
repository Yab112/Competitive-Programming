class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        me = len(piles) - 2
        bob = 0 
        collect = 0
        while me > bob:
          collect += piles[me]
          me -= 2
          bob += 1
        return collect
            