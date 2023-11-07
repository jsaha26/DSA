# https://leetcode.com/problems/word-pattern/

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split()
        return len(set(pattern)) == len(set(s)) == len(set(zip(pattern, s))) and len(pattern) == len(s)
