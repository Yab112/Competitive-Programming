import random 
class Solution:
    def __init__(self, w: List[int]):
        
        self.weights = [0]
        for weight in w:
            self.weights.append(self.weights[-1] + weight)

    def pickIndex(self) -> int:
        left , right = 0, len(self.weights) - 1
        randomNUm = random.randint(1,self.weights[-1])
        while left < right:
            mid = (left + right) // 2
            if self.weights[mid] >= randomNUm:
                right = mid
            else:
                left = mid + 1
        return left - 1
            


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()