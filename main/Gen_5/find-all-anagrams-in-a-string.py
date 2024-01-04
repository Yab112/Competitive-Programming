from collections import Counter
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        p_c = Counter(p)
        l = 0
        r = len(p) - 1
        indices = []
        while r < len(s):
            if Counter(s[l:r+1]) == p_c:
                indices.append(l)
            l += 1
            r+= 1
        return indices