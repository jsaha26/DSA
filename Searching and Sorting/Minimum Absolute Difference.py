# https://leetcode.com/problems/minimum-absolute-difference/

class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        d = defaultdict(list)
        m = float('inf')

        arr.sort()

        for i in range(1, len(arr)):
            dif = arr[i]-arr[i-1]
            m = min(m, dif)
            d[dif].append([arr[i-1], arr[i]]) 

        return d[m]
