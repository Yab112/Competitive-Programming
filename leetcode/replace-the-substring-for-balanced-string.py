class Solution:
    def balancedString(self, s: str) -> int:
        l = 0
        minim = len(s)
        target = len(s)//4
        dec = collections.Counter(s)
        for i,value in enumerate(s):
            dec[value] -= 1
            while l < len(s) and dec["Q"] <= target  and dec["W"] <= target and dec["E"] <= target and dec["R"] <= target:
                temp = s[l]
                dec[temp] += 1
                minim = min(minim,i - l + 1)
                l += 1
        return minim 
                
            
            