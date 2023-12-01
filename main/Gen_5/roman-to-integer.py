class Solution:
    def romanToInt(self, s: str) -> int:
        roman_numerals = {
    'I' : 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
        }
        num_Int,i = 0,0
        while i < len(s):
            if s[i] == "I" and i+1 < len(s) and s[i+1] == "V" :
                num_Int += 4
                i += 2
            elif  s[i] == "I" and i+1 < len(s) and s[i+1] == "X" :
                num_Int += 9
                i += 2
            elif  s[i] == "X" and i+1 < len(s) and s[i+1] == "L" :
                num_Int += 40
                i += 2
            elif s[i] == "X" and i+1 < len(s)  and s[i+1] == "C" :
                num_Int += 90
                i += 2
            elif  s[i] == "C" and i+1 < len(s) and s[i+1] == "D":
                num_Int += 400
                i += 2
            elif s[i] == "C" and i+1 < len(s) and s[i+1] == "M":
                num_Int += 900
                i += 2
            else:
                num_Int += roman_numerals[s[i]]
                i += 1
        return num_Int
        

        