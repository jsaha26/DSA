#https://practice.geeksforgeeks.org/problems/remove-duplicates-from-an-unsorted-linked-list/

#User function Template for python3
'''
		# Node Class
		class Node:
		    def __init__(self, data):   # data -> value stored in node
		        self.data = data
		        self.next = None
	
'''
class Solution:
    def removeDuplicates(self, head):
	
	if not head or not head.next:
            return head

        seen = set()
        curr = head
        prev = None
        
        while curr:
            if curr.data in seen:
                prev.next = curr.next
            else:
                seen.add(curr.data)
                prev = curr
            curr = curr.next
        
        return head
