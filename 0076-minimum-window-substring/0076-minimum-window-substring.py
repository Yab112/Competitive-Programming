class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s or len(t) > len(s):
            return ""
        
        t_count = Counter(t)
        window_count = defaultdict(int)
        
        l = 0
        formed = 0
        required = len(t_count)
        
        min_len = float("inf")
        res = ""
        
        for r in range(len(s)):
            char = s[r]
            window_count[char] += 1
            
            if char in t_count and window_count[char] == t_count[char]:
                formed += 1
            
            while formed == required:
                if r - l + 1 < min_len:
                    min_len = r - l + 1
                    res = s[l:r + 1]
                
                window_count[s[l]] -= 1
                if s[l] in t_count and window_count[s[l]] < t_count[s[l]]:
                    formed -= 1
                l += 1
        
        return res
