# https://leetcode.com/problems/minimum-time-to-make-rope-colorful/

class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        res = 0
        for i in range(1, len(colors)):
            if colors[i] == colors[i - 1]:
                res += min(neededTime[i], neededTime[i - 1])
                neededTime[i] = max(neededTime[i], neededTime[i - 1])
        return res
