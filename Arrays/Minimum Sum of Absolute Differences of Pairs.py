# https://practice.geeksforgeeks.org/problems/minimum-sum-of-absolute-differences-of-pairs/1

class Solution:
    def findMinSum(self, a, b, n):
    
    	a.sort()
    	b.sort()
    
    	sum = 0
    	
    	for i in range(n):
    		sum += abs(a[i] - b[i])
    
    	return sum
