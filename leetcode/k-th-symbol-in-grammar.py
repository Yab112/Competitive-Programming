class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        if n == 1 and k == 1:
            return 0
        mid = pow(2,n-1) //2
        partial = 1
        if k <= mid:
            partial = self.kthGrammar(n-1,k)
        else:
            partial =1 ^ self.kthGrammar(n- 1,k -mid)

        return partial