class Solution:
    def calculate(self,s: str) -> int:  
        stack = []  
        current_result = 0  
        current_number = 0  
        operation = 1  # 1 for addition, -1 for subtraction  
        i = 0  
        while i < len(s):  
            char = s[i]  

            if char.isdigit():  
                current_number = 0  
                while i < len(s) and s[i].isdigit():  
                    current_number = current_number * 10 + int(s[i])  
                    i += 1  
                # Update current result based on the last operation  
                current_result += current_number * operation  
                continue  

            elif char == '+':  
                operation = 1  
            elif char == '-':  
                operation = -1  
            elif char == '(':  
                # Push the current result and operation onto the stack  
                stack.append(current_result)  
                stack.append(operation)  
                current_result = 0  
                operation = 1 
            elif char == ')':  
                current_result *= stack.pop()   
                current_result += stack.pop()  
            elif char != ' ': 
                continue 
            i += 1  

        return current_result

            