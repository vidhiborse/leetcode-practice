class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        # Helper function to count k nodes from a given node
        def get_kth(curr, k):
            while curr and k > 0:
                curr = curr.next
                k -= 1
            return curr

        dummy = ListNode(0, head)
        group_prev = dummy

        while True:
            # Step 1: Find the k-th node from the current group pointer
            kth = get_kth(group_prev, k)
            if not kth:
                break
            group_next = kth.next

            # Step 2: Reverse the k nodes
            prev = kth.next
            curr = group_prev.next
            while curr != group_next:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt

            # Step 3: Connect the reversed group with the rest of the list
            tmp = group_prev.next
            group_prev.next = kth
            group_prev = tmp

        return dummy.next