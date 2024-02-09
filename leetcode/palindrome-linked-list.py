# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        array = []
        while head != None:
            array.append(head.val)
            head = head.next
        l = 0
        r = len(array) - 1
        while l <= r :
            if array[l] != array[r]:
                return False
            r -= 1
            l += 1
        return True
            