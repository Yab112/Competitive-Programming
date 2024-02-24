class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        return [math.factorial(rowIndex) // (math.factorial(k) * math.factorial(rowIndex-k)) for k in range(rowIndex + 1)]