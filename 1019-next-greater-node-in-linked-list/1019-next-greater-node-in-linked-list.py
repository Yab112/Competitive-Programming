# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        arr = [0]*self.c(head)
        stack = []
        cur = head
        i = 0
        while cur:
            while cur and stack and stack[-1][0] < cur.val:
                tmp = stack.pop()
                arr[tmp[1]] = cur.val
            if cur :
                stack.append((cur.val,i))
                cur = cur.next
                i += 1
        return arr
            
    def c(self, head: Optional[ListNode]) -> List[int]:
        cur_node = head
        count = 0
        while cur_node:
            count += 1
            cur_node = cur_node.next
        return count
