class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        r = k -1
        l = 0
        c = 0
        res = 0
        
        for j,i in enumerate(s):
            if i == "a" or i == "e" or i == "i" or i == "o" or i == "u":
                c += 1
            if j - l + 1 == k:
                res = max(res,c)
                if s[l] == "a" or s[l] == "e" or s[l] == "i" or s[l] == "o" or s[l] == "u":
                    c -= 1
                l += 1
            if c == k:
                return k
        return res
            
            