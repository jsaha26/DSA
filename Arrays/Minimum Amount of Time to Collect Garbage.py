# https://leetcode.com/problems/minimum-amount-of-time-to-collect-garbage/

class Solution:
    def garbageCollection(self, g: List[str], t: List[int]) -> int:

        ans = 0
        lastM, lastP, lastG = 0, 0, 0
        countM, countP, countG = 0, 0, 0

        prefix = [0] * (len(t) + 1)

        for i in range(1, len(t) + 1):
            prefix[i] = prefix[i - 1] + t[i - 1]

        for i in range(len(g)):
            for c in g[i]:
                if c == 'M': countM += 1; lastM = i
                if c == 'P': countP += 1; lastP = i
                if c == 'G': countG += 1; lastG = i

        if countM:
            ans += (countM + prefix[lastM])
        if countP:
            ans += (countP + prefix[lastP])
        if countG:
            ans += (countG + prefix[lastG])

        return ans
