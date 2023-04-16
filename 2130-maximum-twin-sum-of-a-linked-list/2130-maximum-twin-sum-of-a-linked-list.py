# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        cur = head 
        count = 0
        while cur:
            cur = cur.next
            count += 1
        cur = head
        stop = count // 2
        index = 1
        while index != stop :
            cur = cur.next
            index +=1
        new_head = cur.next
        cur.next = None
        temp = new_head
        prev = None 
        while temp:
            temp1 = temp.next
            temp.next = prev
            prev = temp
            temp = temp1
        maxm = float(-inf)
        while prev:
            maxm = max(maxm, prev.val+head.val)
            prev = prev.next
            head= head.next
        return maxm
        
            

            
            
        
        
        
                
        