# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        left_dummy = ListNode(0)
        right_dummy = ListNode(0)
        
        left = left_dummy
        right = right_dummy
        
        cur = head
        while cur:
            if cur.val < x:
                left.next = cur
                left = left.next
            else:
                right.next = cur
                right = right.next
            cur = cur.next
        left.next = right_dummy.next
        right.next = None
        return left_dummy.next