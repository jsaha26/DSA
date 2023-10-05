#https://leetcode.com/problems/palindromic-substrings/

class Solution:
    def countSubstrings(self, s: str) -> int:
        
        op = 0
        n = len(s)

        for a in range(n):
            i,j = a,a
            while 0<=i<n and 0<=j<n and s[i]==s[j]:
                op+=1
                i-=1
                j+=1
            i,j = a,a+1
            while 0<=i<n and 0<=j<n and s[i]==s[j]:
                op+=1
                i-=1
                j+=1
        return op
