class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        r= len(palindrome) - 1
        l = 0
        res = ""

        if len(palindrome) ==1 :
            return ""
        while l < r:
            if palindrome[r] == palindrome[l] and palindrome[l] != "a":
                return palindrome[:l] + "a" + palindrome[l + 1:]
                
            l += 1
            r -= 1
        return palindrome[:len(palindrome)-1] + "b"