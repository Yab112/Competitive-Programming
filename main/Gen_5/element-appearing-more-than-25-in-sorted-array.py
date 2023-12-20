from collections import Counter
class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        my_dict = Counter(arr)
        return [a for a,b in my_dict.items() if (b / len(arr)) * 100 > 25][0]     
        