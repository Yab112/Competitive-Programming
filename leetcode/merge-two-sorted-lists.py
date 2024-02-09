# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        temp1 = self.flattner(list1)
        temp2 = self.flattner(list2)
        temp1.extend(temp2)
        temp1.sort()
        return self.linked_list_maker(temp1)
    def flattner(self,head):
        new_array = []
        while head != None:
            new_array.append(head.val)
            head = head.next
        return new_array
    def linked_list_maker(self,array):
        if not len(array):
            return None
        head = ListNode(array[0])
        cur = head
        for i in range(1,len(array)):
            temp = ListNode(array[i])
            cur.next = temp 
            cur = cur.next
        return head