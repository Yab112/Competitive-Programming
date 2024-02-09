from typing import List
from collections import defaultdict

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        win_size = 0
        dec = defaultdict(int)
        p = 0

        for i, value in enumerate(fruits):
            dec[value] += 1
            while  len(dec) > 2:
                dec[fruits[p]] -= 1
                if dec[fruits[p]] == 0:
                    del dec[fruits[p]]
                p += 1
            win_size = max(win_size, i - p + 1)
        return win_size