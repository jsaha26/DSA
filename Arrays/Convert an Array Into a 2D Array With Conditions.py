# https://leetcode.com/problems/convert-an-array-into-a-2d-array-with-conditions/

class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:

        c = defaultdict(int)
        res = []

        for x in nums:

            if len(res) == c[x]:
                res.append([])

            res[c[x]].append(x)
            c[x] += 1
            
        return res
