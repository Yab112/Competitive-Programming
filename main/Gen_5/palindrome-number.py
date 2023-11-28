class Solution:
    def isPalindrome(self, x: int) -> bool:
        new_number = 0
        x_copy = x
        if x < 0:return False
        while x:
            temp = x % 10 
            new_number = new_number * 10 + temp
            x//=10
        return  new_number == x_copy
        
        