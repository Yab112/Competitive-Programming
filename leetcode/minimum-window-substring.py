class Solution:
    def minWindow(self, s: str, t: str) -> str:
        dic_1 = Counter(t)
        dic_2 = defaultdict(int)
        
        l = 0 
        res = float("inf")
        formed_char = 0
        ret = ""
        
        for j, i in enumerate(s):
            if i in dic_1:
                dic_2[i] += 1 
                if dic_2[i] == dic_1[i]:
                    formed_char += 1
                
            while formed_char == len(dic_1):
                if j - l + 1 < res:
                    res = j - l + 1
                    ret = s[l:j + 1]
                
                if s[l] in dic_2:    
                    dic_2[s[l]] -= 1
                    if dic_2[s[l]] < dic_1[s[l]]:
                        formed_char -= 1
                
                l += 1
        
        return ret
