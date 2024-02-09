# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        visited = {}
        counter = 0
        while head is not None:
            if head in visited:
                return head
            visited[head] = counter
            counter += 1
            head = head.next
        return None