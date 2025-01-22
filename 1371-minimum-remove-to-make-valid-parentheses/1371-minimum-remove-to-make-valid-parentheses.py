class Solution:  
    def minRemoveToMakeValid(self, s: str) -> str:  
        result = []  
        balance = 0  

        # First pass to count the balance of parentheses  
        for char in s:  
            if char == '(':  
                balance += 1  
                result.append(char)  
            elif char == ')':  
                if balance > 0:  
                    balance -= 1  
                    result.append(char)  
            else:  
                result.append(char)  

        # Second pass to filter out excess '('  
        final_result = []  
        for char in reversed(result):  
            if char == '(' and balance > 0:  
                balance -= 1  
                continue  
            final_result.append(char)  

        # Join the final result while reversing to original order  
        return ''.join(reversed(final_result))