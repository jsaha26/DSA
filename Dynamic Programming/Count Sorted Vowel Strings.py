# https://leetcode.com/problems/count-sorted-vowel-strings/

class Solution:
    def countVowelStrings(self, n: int) -> int:
        a = e = i = o = u = 1

        while n > 1:
            a, e, i, o, u = a + e + i + o + u, e + i + o + u, i + o + u, o + u, u
            n -= 1

        return a + e + i + o + u
