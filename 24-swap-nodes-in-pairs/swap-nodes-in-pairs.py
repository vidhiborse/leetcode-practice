class Solution(object):
    def swapPairs(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy = ListNode(0)
        dummy.next = head
        current = dummy
        
        while current.next and current.next.next:
            first = current.next
            second = current.next.next
            
            # Reversing the pointers for the pair
            first.next = second.next
            second.next = first
            current.next = second
            
            # Move the pointer two nodes forward
            current = first
            
        return dummy.next