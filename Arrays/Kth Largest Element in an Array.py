class Solution:
    def countGreater(self, A, target):
        count = 0
        for x in A:
            if x > target:
                count += 1
        return count

    def findKthLargest(self, A, k):
        low = min(A)
        high = max(A)
        mid, count = 0, 0

        while low < high:
            mid = low + (high - low) // 2
            count = self.countGreater(A, mid)

            if count >= k: 
                low = mid + 1
            else:
                high = mid

        return low   
