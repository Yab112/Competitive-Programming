# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        left_node = ListNode(0)
        right_node = ListNode(0)
        right = right_node
        left = left_node
        
        cur = head
        counter = 0
        while cur != None:
            if counter % 2 == 0:
                left.next = cur
                left = left.next
            else:
                right.next = cur
                right = right.next
            cur = cur.next
            counter +=1
        left.next = right_node.next
        right.next = None
        return left_node.next
        