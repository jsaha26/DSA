class Solution:
    def findMinSum(self, a, b, n):
    
    	a.sort()
    	b.sort()
    
    	sum = 0
    	
    	for i in range(n):
    		sum += abs(a[i] - b[i])
    
    	return sum
