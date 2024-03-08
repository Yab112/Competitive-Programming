from typing import List

class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        first = {}
        for i,num in enumerate(intervals):
            first[num[0]] = i
        temp = [i for i in first.keys()]
        temp.sort()
        ans = []
        for i in intervals:
            res = self.check(i[1],first,temp)
            ans.append(res)
        return ans
    def check(self,num,dic,arr):
        l = 0
        r = len(arr) - 1
        potential_ans = []
        while l <= r:
            mid = l + ( r - l)//2
            if arr[mid] >= num:
                potential_ans.append(dic[arr[mid]])
                r = mid - 1
            elif arr[mid] < num:
                l = mid + 1
        return potential_ans[-1] if len(potential_ans) > 0 else -1
            
            

       
            
    
       
