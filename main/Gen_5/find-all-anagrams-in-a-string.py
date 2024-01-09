from collections import Counter
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        p_c = Counter(p)
        l = 0
        r = len(p) - 1
        k = len(p)
        indices = []
        while r < len(s):
            if Counter(s[l:r+1]) == p_c:
                indices.append(l)
            if  r + 2 < len(s) and s[r+1] not in p_c:
                l  = r + 2
                r = (l + (k-1))
            else:
                l += 1
                r+= 1
        return indices