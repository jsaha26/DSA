#https://practice.geeksforgeeks.org/problems/-minimum-number-of-coins4426/1

class Solution:
    def minPartition(self, n):
        v = []
    	while(n > 0):
    
    		if(n >= 2000):
    			v.append(2000)
    			n -= 2000
    		elif(n >= 500):
    			v.append(500)
    			n -= 500
    		elif(n >= 200):
    			v.append(200)
    			n -= 200
    		elif(n >= 100):
    			v.append(100)
    			n -= 100
    		elif(n >= 50):
    			v.append(50)
    			n -= 50
    		elif(n >= 20):
    			v.append(20)
    			n -= 20
    		elif(n >= 10):
    			v.append(10)
    			n -= 10
    		elif(n >= 5):
    			v.append(5)
    			n -= 5
    		elif(n >= 2):
    			v.append(2)
    			n -= 2
    		elif(n >= 1):
    			v.append(1)
    			n -= 1
    
    	return v
