# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, head1: Optional[ListNode], head2: Optional[ListNode]) -> Optional[ListNode]:
        if head1 and head2:
            if head1.val <= head2.val:
                sorted_head = ListNode(head1.val) 
                head1 = head1.next
            else:
                sorted_head = ListNode(head2.val)
                head2 = head2.next
            cur = sorted_head
            while head1 and head2 :
                if head1.val <= head2.val:
                    cur.next = ListNode(head1.val) 
                    head1 = head1.next
                else:
                    cur.next = ListNode(head2.val)
                    head2 = head2.next
                cur = cur.next
            if head1:
                cur.next = head1
            else:
                cur.next = head2
            return sorted_head
        elif  head1:return head1
        else: return head2
            