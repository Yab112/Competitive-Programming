class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        def robin_karp(text,pattern,d=256,q=101)->int:
            text_hash = 0
            pattern_hash = 0
            n = len(text)
            m = len(pattern)
            h = 1
            
            for i in range(m-1):
                h = (d * h) % q
            
            for i in range(m):
                pattern_hash = (d * pattern_hash + ord(pattern[i])) % q
                text_hash = (d * text_hash + ord(text[i])) % q
            
            for i in range(n-m + 1):
                if pattern_hash == text_hash and text[i:i+m] == pattern:
                    return i
                else:
                     if i < n - m:
                        text_hash = (d * (text_hash - ord(text[i]) * h) + ord(text[i + m])) % q
                        if text_hash < 0:
                            text_hash += q
            return -1
        if len(needle) > len(haystack):return -1
        return robin_karp(haystack,needle) 