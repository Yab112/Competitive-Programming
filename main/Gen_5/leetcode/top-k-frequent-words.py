class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        dic = Counter(words)
        arr = list(dic.items())
        arr.sort(key = lambda x:(-x[1],x[0]))
        temp = arr[:k]
        return [ i for i,j in temp ]