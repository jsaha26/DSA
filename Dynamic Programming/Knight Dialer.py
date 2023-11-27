# https://leetcode.com/problems/knight-dialer/

class Solution:
    def knightDialer(self, n: int) -> int:
        if n == 1:
            return 10

        u = {
            0: [4, 6],
            1: [6, 8],
            2: [7, 9],
            3: [4, 8],
            4: [0, 3, 9],
            6: [0, 1, 7],
            7: [2, 6],
            8: [1, 3],
            9: [2, 4]
        }

        v = [1] * 10 

        for i in range(2, n + 1):
            temp = [0] * 10  

            for key, val in u.items():
                for j in val: 
                    temp[key] = (temp[key] + v[j])  

            v = temp  

        return sum(v) % 1000000007
