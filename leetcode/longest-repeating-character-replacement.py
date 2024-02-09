from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        dic = defaultdict(int)
        max_count = 0
        max_length = 0
        
        for j in range(len(s)):
            dic[s[j]] += 1
            max_count = max(max_count, dic[s[j]])
            
            if j - l + 1 - max_count > k:
                dic[s[l]] -= 1
                l += 1
                
            max_length = max(max_length, j - l + 1)
        
        return max_length
