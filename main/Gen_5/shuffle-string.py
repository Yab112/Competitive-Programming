class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        new_str = [0]*len(s)
        for i,j in zip(s,indices):
                new_str[j] = i
        return ''.join(new_str)
        