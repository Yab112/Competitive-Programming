# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        length = self.counter(head)
        middle = length // 2
        num = 0
        while num < middle:
            head = head.next
            num += 1
        return head
            
    def counter(self,head):
        counter = 0
        while head != None:
            counter += 1
            head = head.next
        return counter