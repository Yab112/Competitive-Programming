class Solution:
    def hIndex(self, citations: List[int]) -> int:

        #  number of elements on right side is more than arr[mid] just go right side otherwise go on left side
        l,r = 0,len(citations) -1
        n = len(citations)
        while l <= r:
            mid = l + (r - l)//2
            if citations[mid] == n - mid:
                return citations[mid]
            elif citations[mid]  < n - mid:
                l = mid + 1
            else:
                r = mid - 1
        return n -l



        