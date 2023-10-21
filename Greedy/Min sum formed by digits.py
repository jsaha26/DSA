# https://practice.geeksforgeeks.org/problems/min-sum-formed-by-digits3551/1

class Solution:
    def minSum(self, a, n):
        a.sort()
        n1, n2 = 0, 0
        for i in range(n):
            if i % 2 == 0:
                n1 = n1 * 10 + a[i]
            else:
                n2 = n2 * 10 + a[i]
        return n1 + n2
