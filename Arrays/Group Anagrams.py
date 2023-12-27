# https://leetcode.com/problems/group-anagrams/

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}
        for i in strs:
            w = ''.join(sorted(i))
            if w in dic:
                dic[w].append(i)
            else:
                dic[w] = [i]
        return list(dic.values())
