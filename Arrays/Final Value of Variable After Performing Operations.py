# https://leetcode.com/problems/final-value-of-variable-after-performing-operations/

class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        return sum({"--X" : -1, "X--" : -1, "++X" : 1, "X++" : 1}[op] for op in operations)
