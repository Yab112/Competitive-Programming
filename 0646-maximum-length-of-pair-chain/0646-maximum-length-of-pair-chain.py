class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        # if pair j comes before pair i, then the chain ending at i can be extended.
        pairs.sort()
        dp = [1] * len(pairs)

        for i in range(len(pairs)):
            for j in range(i):
                if pairs[j][1] < pairs[i][0]:
                    dp[i] = max(dp[i],dp[j] + 1)
        return max(dp)