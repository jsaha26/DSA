# https://leetcode.com/problems/minimum-sum-of-four-digit-number-after-splitting-digits/

class Solution:
    def minimumSum(self, num: int) -> int:
        a,b,c,d=sorted(str(num))
        return int(a+c) + int(b+d)
