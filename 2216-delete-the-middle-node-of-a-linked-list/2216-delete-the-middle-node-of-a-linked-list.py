# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or head.next == None:
            return None
        dummy_node = ListNode(0)
        dummy_node.next = head
        slow,fast =dummy_node, head
        while fast and fast.next:
            if fast.next.next:
                fast = fast.next.next
            else:
                fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return head
        
        