# https://leetcode.com/problems/diagonal-traverse-ii/

class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        diagonal_groups = defaultdict(list)
        result = []

        for row in range(len(nums)):
            for col in range(len(nums[row])):
                diagonal_groups[row + col].append(nums[row][col])

        # diagonal_groups = {
        #                     0: [1],
        #                     1: [2, 4],
        #                     2: [3, 5, 7],
        #                     3: [6, 8],
        #                     4: [9]
        #                     }



        for diagonal in sorted(diagonal_groups.keys()):
            result.extend(diagonal_groups[diagonal][::-1])

        return result
