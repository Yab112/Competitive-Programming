class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        l = 0 
        r = len(letters) 
        while l < r:
            mid  = l + (r - l)//2
            if letters[mid] > target:
                r = mid 
            else:
                l = mid + 1
        return letters[r] if r < len(letters) else letters[0]