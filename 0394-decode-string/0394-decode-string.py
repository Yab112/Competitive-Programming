class Solution:  
    def decodeString(self, s: str) -> str:  
        s_1, s_2 = [], []  # s_1 for digits, s_2 for characters  
        new_str = ""  
        num = 0  

        for ind, char in enumerate(s):  
            if char.isdigit():   
                num = num * 10 + int(char)  
            elif char == '[':  
                s_1.append(num)  
                s_2.append("") 
                num = 0 
            elif char == ']':   
                temp = s_2.pop()  
                multi = s_1.pop()     
                new_substring = temp * multi  
                if s_2:   
                    s_2[-1] += new_substring  
                else:  
                    new_str += new_substring   
            else:  
                if s_2:  
                    s_2[-1] += char
                else:  
                    new_str += char   

        return new_str