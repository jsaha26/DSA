# https://leetcode.com/problems/divisible-and-non-divisible-sums-difference/

class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        nums1, nums2 = 0, 0
        for i in range(1, n + 1):
            if i % m == 0:
                nums2+=i
            else:
                nums1+=i
        return (nums1 - nums2)
