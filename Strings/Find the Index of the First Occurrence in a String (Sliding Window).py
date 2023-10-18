#https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/

class Solution(object):
    def strStr(self, haystack, needle):
        l,r = 0,len(needle)
        while r <= len(haystack):
            if haystack[l:r] == needle:
                return l
            l += 1
            r += 1
        return -1
