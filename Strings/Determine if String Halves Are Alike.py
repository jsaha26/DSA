# https://leetcode.com/problems/determine-if-string-halves-are-alike

class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        def count_vowels(string):
            return sum(1 for char in string if char in 'aeiouAEIOU')

        mid_point = len(s) // 2
        return count_vowels(s[:mid_point]) == count_vowels(s[mid_point:])
