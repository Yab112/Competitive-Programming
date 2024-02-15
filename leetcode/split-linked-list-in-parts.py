# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def __init__(self):
        self.head = None

    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        cur = head
        arr = []
        length = self.return_len(head)

        if k >= length:
            while cur:
                arr.append(ListNode(cur.val))
                cur = cur.next
            for i in range(k - length):
                arr.append(None)
                    
        else:
            part_size,extra_parts = divmod(length,k)
            cur = head
            for _ in range(k):
                part_head = ListNode()
                part_cur = part_head
                part_counter = part_size + ( 1 if extra_parts > 0 else 0)
                while part_counter > 0:
                    part_cur.next = ListNode(cur.val)
                    part_cur = part_cur.next
                    cur = cur.next
                    part_counter -= 1
                arr.append(part_head.next)
                if extra_parts > 0:
                    extra_parts -= 1
        return arr

    def return_len(self, head):
        length = 0
        cur = head
        while cur:
            length += 1
            cur = cur.next
        return length
