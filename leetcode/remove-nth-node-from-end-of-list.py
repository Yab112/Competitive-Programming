# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode] :
        len_list = self.counter(head)
        if len_list == 1:
            return None
        elif len_list - n == 0:
            return head.next
        else:
            temp = head
            for _ in range(len_list - n - 1):
                temp = temp.next
            if temp.next != None:
                temp.next = temp.next.next
            else:
                temp.next = None
            return head
    
    def counter(self,head):
        count = 0 
        cur = head 
        while cur != None:
            count += 1
            cur = cur.next
        return count