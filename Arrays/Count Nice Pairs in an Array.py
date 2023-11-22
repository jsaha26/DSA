# https://leetcode.com/problems/count-nice-pairs-in-an-array/

class Solution:
    def countNicePairs(self, nums: List[int]) -> int:

        def reverse_num(x):
            return int(str(x)[::-1])

        mod = 10**9 + 7
        seen = {}
        nice_pairs = 0

        for i in range(len(nums)):
            rev_i = reverse_num(nums[i])
            diff = nums[i] - rev_i

            if diff in seen:
                nice_pairs = (nice_pairs + seen[diff]) % mod

            seen[diff] = (seen.get(diff, 0) + 1) % mod

        return nice_pairs
