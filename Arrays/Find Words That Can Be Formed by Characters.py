# https://leetcode.com/problems/find-words-that-can-be-formed-by-characters/description/

class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        length=0
        for i in words:
            for j in i:
                if chars.count(j) < i.count(j): 
                    break
            else:
                length+=len(i)
        return length
