class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        res = 0
        dict_latt = {}
        for i, num in enumerate(s):
            if num not in dict_latt:
                dict_latt[num] = i
            else:
                res = max(res,len(dict_latt))
                temp = dict_latt[num]
                while l < temp + 1:
                    del dict_latt[s[l]]
                    l += 1
                dict_latt[num] = i
        return max(res,len(dict_latt)) 
            
