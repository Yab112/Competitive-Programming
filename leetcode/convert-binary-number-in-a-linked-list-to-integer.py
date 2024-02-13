# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        lent = self.get_len(head)
        used = lent - 1
        cur = head 
        binn = 0
        while cur != None:
            binn += ( (2 ** (used) )* cur.val)
            used -= 1
            cur = cur.next
        return binn
    def get_len(self,head):
        cur  = head
        le = 0
        while cur != None:
            le += 1
            cur = cur.next
        return le
            