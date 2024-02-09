class Solution:
    def maxScore(self, s: str) -> int:
        prefix_sum = [0] * len(s)
        no_0 = 0
        maximum = float('-inf')  
        prefix_sum[0] = int(s[0])
        
        for i in range(1, len(s)):
            prefix_sum[i] = prefix_sum[i - 1] + int(s[i])
        no_1 = prefix_sum[-1]
        for j, num in enumerate(s):
            if j == len(s) - 1:
                break
            elif int(num) == 0:
                no_0 += 1
            else:
                no_1 -= 1
            maximum = max(maximum, no_1 + no_0)
        
        return maximum 