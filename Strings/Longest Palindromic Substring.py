class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n <= 1:
            return s

        m, p, q = 0, 0, 0

        for i in range(n):
            for j in range(i+1, n+1):
                ss = s[i:j]
                if ss == ss[::-1] and len(ss) > m:
                    m = len(ss)
                    p = i
                    q = j

        return s[p:q]
