# https://leetcode.com/problems/frequency-of-the-most-frequent-element/

class Solution:
    def possible(self, nums, mid, k):
        window_sum = sum(nums[:mid])  # Calculate the sum of the first 'mid' elements in nums
        total_sum = nums[mid - 1] * mid  # Calculate the total sum of 'mid' elements

        if total_sum - window_sum <= k:  # Check if the difference between total_sum and window_sum is less than or equal to 'k'
            return True

        j = 0
        for i in range(mid, len(nums)):
            window_sum -= nums[j]  # Adjust window_sum by subtracting the first element in the current window
            window_sum += nums[i]  # Adjust window_sum by adding the next element in the current window
            total_sum = nums[i] * mid  # Update total_sum based on the current element and 'mid'

            if total_sum - window_sum <= k:  # Check if the difference between total_sum and window_sum is less than or equal to 'k'
                return True
            j += 1

        return False

    def maxFrequency(self, nums: List[int], k: int) -> int:
        l, h, ans = 1, len(nums), 0  
        nums.sort()  

        while l <= h:
            mid = l + (h - l) // 2  

            if self.possible(nums, mid, k):  # Check if it's possible to make a subarray with size 'mid' and a sum difference less than or equal to 'k'
                ans = mid 
                l = mid + 1  
            else:
                h = mid - 1  

        return ans  
