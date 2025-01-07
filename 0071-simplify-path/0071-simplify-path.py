class Solution:
    def simplifyPath(self, path: str) -> str:
        result = re.findall(r'[^/]+|/', path)
        stack = []
        for char in result:
            if char == "..":
                if stack:
                    stack.pop()
                else:
                    stack.append("/")
            elif char == "/" or char == ".":
                if len(stack) == 0 and char == "/":
                    stack.append(char)
                else:
                    continue
            else:
                if len(stack) == 1 and len(stack[0]) == 1:
                    stack.append(char)
                else:
                    stack.append("/" + char)
        return "".join(stack) if stack else "/"
                
            