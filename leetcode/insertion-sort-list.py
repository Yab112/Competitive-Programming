# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return 
        if head and not head.next:
            return head
        else:
            cur = head.next
            while cur :
                temp = head
                while  temp != cur:
                    if cur.val < temp.val:
                        cur.val,temp.val = temp.val,cur.val
                    temp = temp.next
                temp = head
                cur = cur.next
            return head
            