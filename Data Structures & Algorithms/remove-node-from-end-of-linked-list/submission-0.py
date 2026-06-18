# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        left = dummy
        right = head
        
        # Step 1: Create a gap of 'n' nodes by moving right pointer forward
        for _ in range(n):
            right = right.next
            
        # Step 2: Move both pointers until right hits the end of the list
        while right:
            left = left.next
            right = right.next
            
        # Step 3: left is now pointing to the node BEFORE the one to delete
        left.next = left.next.next
        
        return dummy.next