class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        last_occurance = {c:i for i,c in enumerate(s)}
        stack = []
        lst = set()

        for i,char in enumerate(s):
            if char not in lst:
                while stack and stack[-1] > char and last_occurance[stack[-1]] > i:
                    lst.remove(stack.pop())
                stack.append(char)
                lst.add(char)
        return "".join(stack)