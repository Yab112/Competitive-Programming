# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
def reverse(nums,rp,lp):
    while lp < rp :
        nums[lp],nums[rp] =  nums[rp],nums[lp]
        lp += 1
        rp -= 1
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        nums = []
        cur = head
        while cur :
            nums.append(cur.val)
            cur=cur.next
        lp ,rp = 0, k-1
        while rp < len(nums):
            reverse(nums,rp,lp)
            rp += k
            lp +=k
        new_head  =ListNode(nums[0])
        new_cur = new_head
        for i in range(1,len(nums)):
            new_cur.next = ListNode(nums[i])
            new_cur = new_cur.next
        return new_head      
            
    
            
            
            
        