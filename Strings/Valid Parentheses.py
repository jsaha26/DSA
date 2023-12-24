# https://leetcode.com/problems/valid-parentheses/

class Solution(object):
    def isValid(self, s):
        stack = [] # only to use append and pop
        opening_chars = "({["
        pairs = {
            '(': ')',
            '{': '}',
            '[': ']'
        }
        for i in s:
            if i in opening_chars:
                stack.append(i)
            elif len(stack) == 0 or i != pairs[stack.pop()]:
                return False

        return len(stack) == 0
