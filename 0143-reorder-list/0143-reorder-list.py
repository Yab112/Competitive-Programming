# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return 
        stack = []
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        middle = slow
        slow = middle.next 
        while slow:
            stack.append(slow)
            slow = slow.next

        middle.next = None
        current = head
        while stack:
            popped_node = stack.pop()
            next_elem = current.next

            current.next = popped_node
            popped_node.next = next_elem
            current = next_elem  
                