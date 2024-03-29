class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        dic  = {}
        for i in arr:
            if i not in dic:
                dic[i ] = 1
            else:
                dic[i] += 1
        h = sorted(dic.items(), key=lambda item: item[1])
        differnce, count = 0, 0
        while differnce < len(arr)/2:
            tmp = h.pop()
            count += 1
            differnce += tmp[1]
        return count 
            
            