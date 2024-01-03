class Solution:
    def isPalindrome(self, s: str) -> bool:
        my_str = "".join(i for i in s if i.isalnum()).lower()
        l = 0
        r = len(my_str) - 1
        flag = True
        while l <= r:
            if my_str[l] != my_str[r]:
                flag = False
                break
            r -= 1
            l += 1
        return flag