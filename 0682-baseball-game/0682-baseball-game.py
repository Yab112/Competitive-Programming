class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []  

        for op in operations:  
            if op.lstrip('-').isdigit():  # check if op is a number  
                stack.append(int(op))  
            elif op == "C":  # cancel the last score  
                if stack:  
                    stack.pop()  
            elif op == "D":  # double the last score  
                if stack:  
                    stack.append(2 * stack[-1])  
            elif op == "+":  # sum of the last two scores  
                if len(stack) >= 2:  
                    stack.append(stack[-1] + stack[-2])  

        return sum(stack) 
                