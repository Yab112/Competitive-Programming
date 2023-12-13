class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        positives = [i for i in nums if i > 0]
        negatives =[i for i in nums if i<=0]
        result =[]
        for i,j in list(zip(positives,negatives)):
            result.append(i)
            result.append(j)
        return result
