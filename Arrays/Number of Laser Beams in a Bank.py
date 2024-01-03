# https://leetcode.com/problems/number-of-laser-beams-in-a-bank/

class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        prev,res = bank[0].count("1"),0
        for i in range(1,len(bank)):
            if ones:= bank[i].count("1"):
                res += (ones*prev)
                prev = ones
        return res
