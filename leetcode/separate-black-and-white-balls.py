class Solution:
    def minimumSteps(self, s: str) -> int:
        num_o = 0
        res = 0
        for i in range(len(s) - 1,-1,-1):
            if s[i] == "0":
                num_o += 1
            elif s[i] == "1":
                res += num_o
        return res
                