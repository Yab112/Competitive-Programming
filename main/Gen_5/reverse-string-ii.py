class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        result = ""
        i = 0
        while i < len(s):
          
            if i + k <= len(s):
                result += s[i:i+k][::-1]
            else:
                result += s[i:][::-1]
            i += k

            if i < len(s):
                result += s[i:i+k]
            i += k
        
        return result