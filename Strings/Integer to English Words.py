# https://leetcode.com/problems/integer-to-english-words/

class Solution(object):
    def numberToWords(self, num):
        if num == 0:
            return "Zero"
        return self.helper(num)

    def helper(self, num):
        belowTwenty = [
            "", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine",
            "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen",
            "Eighteen", "Nineteen"
        ]
        tens = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]

        if num < 20:
            s = belowTwenty[num]
        elif num < 100:
            s = tens[num // 10] + " " + belowTwenty[num % 10]
        elif num < 1000:
            s = self.helper(num // 100) + " Hundred " + self.helper(num % 100)
        elif num < 1000000:
            s = self.helper(num // 1000) + " Thousand " + self.helper(num % 1000)
        elif num < 1000000000:
            s = self.helper(num // 1000000) + " Million " + self.helper(num % 1000000)
        else:
            s = self.helper(num // 1000000000) + " Billion " + self.helper(num % 1000000000)

        return strip(s)
