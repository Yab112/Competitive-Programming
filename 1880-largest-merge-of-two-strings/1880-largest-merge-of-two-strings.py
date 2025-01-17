class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        p_w1 = p_w2 = 0 
        res = ""
        while p_w1 < len(word1) and p_w2 < len(word2):
            if word1[p_w1:] > word2[p_w2:]:
                res+= word1[p_w1]
                p_w1 +=1
            else:
                res+=word2[p_w2]
                p_w2+=1
        if len(word1) > p_w1:
            res += word1[p_w1:]
        elif len(word2) > p_w2:
            res += word2[p_w2:]
        return res


        