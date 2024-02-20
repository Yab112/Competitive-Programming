class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        result = []
        dic = {}
        for i in points:
            if self.cal(i) not in dic:
                dic[self.cal(i)] = []
            dic[self.cal(i)].append(i)
        res = [x for x in dic.keys()]
        res.sort()
        for i in  res[:k]:
            result.extend(dic[i])
        return result[:k]
    def cal(self,dis):
        return sqrt(dis[0] ** 2 + dis[1] ** 2)