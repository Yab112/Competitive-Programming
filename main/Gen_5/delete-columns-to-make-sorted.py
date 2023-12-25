class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        count =0
        for col in range(len(strs[0])):
            temp = []
            for row in range(len(strs)):
                temp.append(strs[row][col])
            if sorted(temp) != temp:
                count +=1
            temp = []
        return count