# https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/

class Solution(object):
    def removeDuplicates(self, s):
        
        stack = []
    
        for char in s:
            if stack and stack[-1] == char:
                stack.pop()
            else:
                stack.append(char)
        
        return ''.join(stack)
