class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        l1 = l2 = k =0
        while l1 < len(g) and l2 < len(s):
           if g[l1] <= s[l2]:
               k += 1
               l1 += 1
               l2+= 1
           elif g[l1] > s[l2]:
                l2 += 1
        return k
            
            
            