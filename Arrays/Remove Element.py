#https://leetcode.com/problems/remove-element/

class Solution(object):
    def removeElement(self, nums, val):
        nums[:] = [x for x in nums if x != val]
        return len(nums)
