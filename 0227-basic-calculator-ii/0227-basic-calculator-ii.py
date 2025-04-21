class Solution:  
    def calculate(self, s: str) -> int:  
        stack = []  
        last_operator = "+"  
        number = 0  
        s = s.replace(' ', '')  

        for i in range(len(s)):  
            if s[i].isdigit():  
                number = number * 10 + int(s[i])  

            if s[i] in "+-*/" or i == len(s) - 1:  
                if last_operator == "+":  
                    stack.append(number)  
                elif last_operator == "-":  
                    stack.append(-number)  
                elif last_operator == "*":  
                    stack[-1] = stack[-1] * number  
                elif last_operator == "/":  
                    stack[-1] = int(stack[-1] / number)    
                
                number = 0  
                last_operator = s[i]   

        return sum(stack)  