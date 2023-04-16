# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        count = 1
        while cur.next !=None:
            cur = cur.next
            count += 1
        num = count // 2
        arr = []
        index = 1
        cur = head
        while cur :
            if cur and index == num + 1:
                return cur
            cur = cur.next
            index += 1
       
       
                
        
        