class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        i = 0
        while i < len(s):
            if s[i] == "(":
                stack.append(i)
                i += 1
            elif s[i] == ")":
                l = stack.pop()
                lf = s[:l]
                rev=s[l+1:i][::-1]
                rt = s[i+1:]
                s = lf + rev + rt
                i-=1
            else:
                i += 1
        return s
