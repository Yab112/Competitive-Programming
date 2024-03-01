class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False
        temp = log(n,3) 
        return 3 ** ceil(temp)  == n
        
        