class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxsum, currsum = nums[0],0
        for i in nums:

            if currsum < 0:
                currsum = 0

            currsum += i 

            if maxsum < currsum:
                maxsum = currsum

        return maxsum
