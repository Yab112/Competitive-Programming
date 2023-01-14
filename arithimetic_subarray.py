class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        arr=[]
        i=0
        arr = [True]*len(l)
        while i < len(l):
            yab=nums[l[i]:r[i]+1]
            yab.sort()
            flag=False
            for j in range(len(yab)-2):
                if yab[j+1]-yab[j] != yab[j+2]-yab[j+1]:
                    arr[i]= False
            i+=1
        return arr
