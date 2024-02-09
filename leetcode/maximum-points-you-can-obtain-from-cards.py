class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        j = len(cardPoints) - k
        i = 0
        holder = sum(cardPoints[j:])
        maxim = holder
        while j < len(cardPoints):
            holder += (cardPoints[i] - cardPoints[j])
            maxim = max(maxim,holder)
            j += 1
            i += 1
        return maxim 
        