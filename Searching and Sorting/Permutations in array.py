#https://practice.geeksforgeeks.org/problems/permutations-in-array1747/1

class Solution:
    def isPossible(self,a, b, n, k):
        return True if all(x + y >= k for x, y in zip(sorted(a), sorted(b, reverse=True))) else False
