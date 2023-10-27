#https://leetcode.com/problems/happy-number/

class Solution:
    def isHappy(self, n: int) -> bool:

        def sumsq(n):
            s = 0
            while n > 0:
                s += (n % 10) ** 2
                n //= 10
            return s

        seen = set()
        while n != 1 and n not in seen:
            seen.add(n)
            n = sumsq(n)

        return n == 1
