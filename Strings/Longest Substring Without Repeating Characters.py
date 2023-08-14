class Solution:
    def lengthOfLongestSubstring(self, s):
        st = 0
        m = 0
        d = {}
        
        for i, v in enumerate(s):
            if v in d and st <= d[v]:
                st = d[v] + 1
            d[v] = i
            m = max(m, i - st + 1)
        
        return m
