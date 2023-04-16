# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        fast = head 
        while n > 0 :
            fast = fast.next
            n  = n - 1
        demi =  ListNode()
        demi.next = head
        slow  = demi
        while fast  :
            fast= fast.next
            slow = slow.next
        slow.next = slow.next.next
        return demi.next
        
             