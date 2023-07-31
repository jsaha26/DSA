class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        currmax, currmin = 1,1

        for n in nums:

            if n == 0:
                currmax, currmin = 1,1

            temp = currmax * n

            currmax = max(temp, n*currmin, n)
            currmin = min(temp, n*currmin, n)
            res = max(currmax, res)

        return res
