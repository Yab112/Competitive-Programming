# Definition for singly-linked list.  
class ListNode:  
    def __init__(self, val=0, next=None):  
        self.val = val  
        self.next = next  

class Solution:  
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:  
        if not head:  
            return None 
        dummy_node = ListNode(0)  
        dummy_node.next = head   
        curr, prev = head, dummy_node  
        while curr:  
            if curr.val == val:  
                prev.next = curr.next  
            else:  
                prev = curr   
            curr = curr.next   
        return dummy_node.next  