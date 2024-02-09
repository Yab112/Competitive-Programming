class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        l = 0
        dic = defaultdict(int)
        max_seen = float("-inf")
        res = float("-inf")
        
        for i in range(len(answerKey)):
            dic[answerKey[i]] += 1
            max_seen = max(max_seen,dic[answerKey[i]])
            
            while (i - l + 1) - max_seen > k:
                dic[answerKey[l]] -= 1
                l += 1
            res = max(res,i - l + 1)
        return res 
            
            
        