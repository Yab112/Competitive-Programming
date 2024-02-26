class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last = {}
        res = []
        max_pos =start = 0
        for i,ch in enumerate(s):
            last[ch] = i
    
    
        for i,ch in enumerate(s):
            max_pos = max(max_pos,last[ch])
            
            if i == max_pos:
                res.append(max_pos - start + 1)
                start = i + 1
        return res
            
            
            
        