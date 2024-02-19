class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = [0]
        res = 0
        for i in s:
            if i == "(":
                stack.append(0)
            else:
                temp = stack.pop()
                res = max(1,temp * 2)
                stack[-1] += res
        return stack.pop()







        