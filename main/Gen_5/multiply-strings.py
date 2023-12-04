class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        num_1 = 0
        num_2 = 0  
        for i in num1:
            num_1 =num_1*10 + ord(i) - ord('0')
        for j in num2:
            num_2 = num_2 * 10 + ord(j) - ord("0")
        return str(num_1 * num_2 )
