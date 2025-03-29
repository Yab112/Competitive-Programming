class Solution:  
    def longestPalindrome(self, s: str) -> str:  
        n = len(s)
        if n <= 1:return s
        start,end = 0,0
        def expand_to_left_right(left:int,right:int)->tuple:
            while left >= 0 and right < n and s[left] == s[right]:
                left -= 1
                right += 1
            return left + 1,right - 1
        
        for i in range(n):
            left1,right1 = expand_to_left_right(i,i)
            left2,right2 = expand_to_left_right(i,i+1)

            if right1 - left1  > end - start :
                start ,end = left1,right1
            if right2 - left2 > end - start:
                start ,end = left2,right2
        return s[start:end + 1]
