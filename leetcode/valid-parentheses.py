class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closing = {"}": "{", "]": "[", ")": "("}
        if len(s) == 1:
            return False
        for i in s:
            if i in closing.values():
                stack.append(i)
            else:
                if not stack:
                    return False  
                temp = stack.pop()
                if temp != closing[i]:
                    return False
        return len(stack) == 0
