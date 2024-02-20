class Solution:
    def myPow(self, x: float, n: int) -> float:
        def pow(x = x,n = abs(n)):
            if n == 0 :return 1
            v = pow(x,n//2)
            if n % 2 == 0:
                return v * v
            else:
                return x * v *v
        f = pow()
        return float(f) if n > 0 else 1/f
        