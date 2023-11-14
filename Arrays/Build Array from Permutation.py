# https://leetcode.com/problems/build-array-from-permutation/submissions/1098791178/

class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        return [nums[i] for i in nums]
