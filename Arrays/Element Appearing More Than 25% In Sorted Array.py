# https://leetcode.com/problems/element-appearing-more-than-25-in-sorted-array/

# class Solution:
#     def findSpecialInteger(self, arr: List[int]) -> int:
#         return statistics.mode(arr)

class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        target_count = len(arr) // 4
        for i in arr:
            if arr.count(i) > target_count:
                return i
