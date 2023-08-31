#https://practice.geeksforgeeks.org/problems/multiply-two-linked-lists

MOD = 10**9+7
# your task is to complete this function
# Function should return an integer value
# head1 denotes head node of 1st list
# head2 denotes head node of 2nd list

'''
class node:
    def __init__(self):
        self.data = None
        self.next = None
'''
def multiplyTwoList(head1, head2):
    n1, n2 = 0,0
    
    while head1:
        n1 = (n1 * 10 + head1.data) % MOD
        head1 = head1.next
    
    while head2:
        n2 = (n2 * 10 + head2.data) % MOD
        head2 = head2.next
    
    return (n1 * n2) % MOD  
