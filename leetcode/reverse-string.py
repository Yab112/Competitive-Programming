class Solution:
    def rev(self,s,left,right):
        if left >= right:
            return
        s[left],s[right] = s[right],s[left]
        left += 1
        right -= 1
        self.rev(s,left,right)
    def reverseString(self, s: List[str]) -> None:
        self.rev(s,0,len(s)-1)
        
        """
        Do not return anything, modify s in-place instead.
        """
        