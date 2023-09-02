class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        return [s.find(c) for c in s] == [t.find(c) for c in t]
