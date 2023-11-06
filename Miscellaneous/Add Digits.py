# https://leetcode.com/problems/add-digits/submissions/1092953676/

class Solution:
    def addDigits(self, num: int) -> int:
        while num > 9:
            sum = 0
            while num:
                sum += num%10
                num = num//10
            num = sum
        return num
