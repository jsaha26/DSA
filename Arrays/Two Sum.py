# https://leetcode.com/problems/two-sum/

class Solution(object):
    def twoSum(self, nums, target):
        seen = {}

        for i in range(len(nums)):

            diff = target - nums[i]

            if diff in seen:
                return [seen[diff], i]

            seen[nums[i]] = i
