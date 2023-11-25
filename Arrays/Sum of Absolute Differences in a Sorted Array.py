class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        res = []
        s=0
        n = len(nums)
        for i in range(1,n):
            s+=nums[i]-nums[0]
        res.append(s)
        for i in range(1,n):
            diff = nums[i]-nums[i-1]
            s += diff*i
            s -= diff *(n-i)
            res.append(s)
        return res
