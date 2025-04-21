class Solution:  
    def parseBoolExpr(self, expression: str) -> bool:  
        boolean_stack = []  
        lgc_stack = []  
        i = 0  
        
        while i < len(expression):  
            char = expression[i]  
            if char in ["!", "&", "|"]:  
                lgc_stack.append(char)  
            elif char == "(":  
                boolean_stack.append(char)  
            elif char == ")":  
                false_count = true_count = 0  
                
                while boolean_stack and boolean_stack[-1] != "(":  
                    val = boolean_stack.pop()  
                    if val == "t":  
                        true_count += 1  
                    elif val == "f":  
                        false_count += 1  
                
                # Pop the "("  
                if boolean_stack and boolean_stack[-1] == "(":  
                    boolean_stack.pop()  
                
                # Get the logical operator  
                if lgc_stack:  
                    op = lgc_stack.pop()  
                    if op == "!":  
                        # Negation  
                        boolean_stack.append("f" if true_count > 0 else "t")  
                    elif op == "&":  
                        # AND  
                        boolean_stack.append("t" if false_count == 0 else "f")  
                    elif op == "|":  
                        # OR  
                        boolean_stack.append("t" if true_count > 0 else "f")  
            else:  
                boolean_stack.append(char)  
            i += 1  
        
        return boolean_stack.pop() == "t"  