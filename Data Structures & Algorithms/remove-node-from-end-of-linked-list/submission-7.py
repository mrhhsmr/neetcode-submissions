# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        total = 0
        cur = head
        while cur:
            cur = cur.next
            total += 1
        
        removeIndex = total - n
        i = 0
        dummy = ListNode(-1, head)
        cur = dummy;
        while i < removeIndex:
            cur = cur.next
            i += 1
        
        cur.next = cur.next.next
        return dummy.next
        
        