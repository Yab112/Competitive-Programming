class Solution:
    def numberOfWays(self, s: str) -> int:
        zeroone = [0] * len(s)
        onezero = [0] *len(s)
        zeros = 0
        ones = 0
        res = 0
        for i,num in enumerate(s):
            if num == "0":
                zeros += 1
            if num == "1":
                zeroone[i] = zeros
        for i,num in enumerate(s):
            if num == "1":
                ones += 1
            if num == "0":
                onezero[i] = ones
        pref_zero_one = [0] * len(s)
        pref_zero_one[0] = zeroone[0]
        
        for i in range(1,len(zeroone)):
            pref_zero_one[i] = pref_zero_one[i - 1] + zeroone[i]
            
        pref_one_zero = [0] * len(s)
        pref_one_zero[0] = zeroone[0]
        
        for i in range(1,len(onezero)):
            pref_one_zero[i] = pref_one_zero[i - 1] + onezero[i]
            
            
        for i in range(1,len(s)):
            if s[i] == "0":
                res += pref_zero_one[i - 1]
            else:
                res += pref_one_zero[i - 1]
        return res
            
            
        