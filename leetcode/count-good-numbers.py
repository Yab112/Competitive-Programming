class Solution:
    def countGoodNumbers(self, n: int) -> int:
        mode = 10 ** 9 + 7
        
        def pow(x,n):
            if  n == 0: return 1

            v = pow(x,n//2)
            if n % 2 == 0:
                return (v * v) % mode
            else:
                return (x * v *v) % mode
                
        even = int(n//2 + int(n%2 != 0))
        odd = int(n//2)
        e = pow(5,even)
        o = pow(4,odd)
        return (e * o )% mode
        