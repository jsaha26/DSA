# https://leetcode.com/problems/arithmetic-subarrays/

class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        
        ans=[1]*len(l)
        
        for i in range(len(l)):
            s=nums[l[i]:r[i]+1]
            s.sort()
            
            for v in range(len(s)-1):
                if (s[v+1]-s[v])!=(s[1]-s[0]):
                    ans[i]=0
                    break
        return ans
