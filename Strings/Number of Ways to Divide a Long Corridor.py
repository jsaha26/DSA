# https://leetcode.com/problems/number-of-ways-to-divide-a-long-corridor/

class Solution:
    def numberOfWays(self, corridor: str) -> int:

        ways, seats, plants = 1, 0, 0

        for c in corridor:
            if c == 'S':
                if seats == 2:
                    # multiply the counts of plants (+1) in between every 2 seats
                    ways = (ways * (plants + 1)) % 1000000007
                    seats = plants = 0
                seats += 1
            # only count plants after you've seen 2 seats (ignore in-between plants)
            elif seats == 2:
                plants += 1

        # ensure the last section has 2 seats i.e. the total number of seats is >=2 and even
        return ways if seats == 2 else 0
