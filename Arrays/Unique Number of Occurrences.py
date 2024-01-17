# https://leetcode.com/problems/unique-number-of-occurrences/

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        freq = {}
    
        for i in arr:
            if i not in freq:
                freq[i] = 0
            freq[i] += 1
    
        return len(freq) == len(set(freq.values()))
