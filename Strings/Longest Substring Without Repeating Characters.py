class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        maxlen = 0
        d = {} # lookup
        for i,c in enumerate(s):
            if c in d and start <= d[c]:
                start = d[c] + 1
            else:
                maxlen = max(maxlen, i - start + 1)
            d[c] = i

        return maxlen
