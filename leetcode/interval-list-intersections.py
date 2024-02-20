class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        if len(firstList) == 0 or len(secondList) == 0:
            return []
        f = s = 0
        res = []
        while f < len(firstList) and s < len(secondList):
            temp1 = max(firstList[f][0],secondList[s][0])
            temp2 = min(firstList[f][1],secondList[s][1])
            

            if temp1 <= temp2:
                res.append([temp1,temp2])
            if firstList[f][1] < secondList[s][1]:
                f +=1
            else:
                s += 1
        return res