class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        arr.sort()
        arr[0] = 1 if arr[0]!=1 else arr[0]

        largest = arr[0]
        
        arr = [largest := largest + 1 if abs(largest - num) else num for num in arr]
        return largest 
        