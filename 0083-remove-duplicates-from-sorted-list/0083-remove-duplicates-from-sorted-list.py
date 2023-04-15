# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        last = head
        if head and head.next :
            cur = last.next
            while cur :
                if cur.val != last.val:
                    last.next = cur
                    last = cur
                cur = cur.next
            last.next = None
            
        return head