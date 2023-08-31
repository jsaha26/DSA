class Solution:
    def segregate(self, head):
        if not head or not head.next:
            return head
        
        # Initialize three pointers for the three segments: 0, 1, and 2.
        zero_head = zero_tail = Node(0)
        one_head = one_tail = Node(0)
        two_head = two_tail = Node(0)
        
        curr = head
        
        while curr:
            if curr.data == 0:
                zero_tail.next = curr
                zero_tail = zero_tail.next
            elif curr.data == 1:
                one_tail.next = curr
                one_tail = one_tail.next
            else:
                two_tail.next = curr
                two_tail = two_tail.next
            curr = curr.next
        
        # Connect the segments in the required order: 0s -> 1s -> 2s.
        zero_tail.next = one_head.next if one_head.next else two_head.next
        one_tail.next = two_head.next
        
        # Set the tails of the 1s and 2s segments to None to terminate the list.
        one_tail.next = None
        two_tail.next = None
        
        # Return the head of the new list starting from the 0s segment.
        return zero_head.next
