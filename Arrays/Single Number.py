class Solution(object):
    def singleNumber(self, nums):
        result = 0
        for x in nums:
            result ^= x
        return result
