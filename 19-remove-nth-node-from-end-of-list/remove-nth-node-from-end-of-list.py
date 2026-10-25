# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        dummy = ListNode(0, head)
        slow = dummy
        fast = dummy
        
        # Advance fast pointer by n + 1 steps so there is a gap of n nodes between slow and fast
        for _ in range(n + 1):
            fast = fast.next
            
        # Move both pointers until fast reaches the end of the list
        while fast is not None:
            slow = slow.next
            fast = fast.next
            
        # Remove the Nth node from the end
        slow.next = slow.next.next
        
        return dummy.next