# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head
        
        # Fast pointer moves twice as fast, so check fast and fast.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
            # If they meet, a cycle is detected
            if slow == fast:
                return True
                
        return False