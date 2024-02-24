class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for i in s:
            if i != ']':
                stack.append(i)
            else:
                temp = ""
                while stack[-1] != '[':
                    temp = stack.pop() + temp
                stack.pop()  # Discard '['
                
                number = ""
                while stack and stack[-1].isdigit():
                    number = stack.pop() + number
                
                stack.append(temp * int(number))
        
        return "".join(stack)
