class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # find the window it self by binary search method 
        l = 0
        r = len(arr) - k

        while l < r:
            mid = l + ( r - l) //2
            if arr[mid + k] - x < x - arr[mid]:
                l = mid + 1
            else:
                r = mid 
        return arr[l:l +k]
            