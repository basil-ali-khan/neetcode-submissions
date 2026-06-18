# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         # self.val = val
#         # self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return
            
        # Step 1: Find the middle of the list
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        # Second half starts after slow pointer
        second = slow.next
        slow.next = None  # Cut the list into two separate halves
        
        # Step 2: Reverse the second half
        prev = None
        curr = second
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
            
        # Step 3: Merge the two halves alternatingly
        first = head
        second = prev  # 'prev' is the head of the reversed second half
        
        while second:
            tmp1, tmp2 = first.next, second.next
            
            first.next = second
            second.next = tmp1
            
            first = tmp1
            second = tmp2