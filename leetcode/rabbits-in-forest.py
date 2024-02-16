from typing import List
from collections import Counter

class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        dic = {}
        res = 0
        for i in answers:
            if i == 0:
                res += 1
            else:
                if i not in dic or dic[i] == i:
                    dic[i] = 0
                    res +=i + 1
                else:
                    dic[i] += 1
        return res


