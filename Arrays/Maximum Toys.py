# In a toy shop there are a number of toys presented with several various – priced toys in a specific order. You have a limited budget and would like to select the greatest number of consecutive toys that fit within the budget. Given prices of the toys and your budget, what is the maximum number of toys that can be purchased for your child?

def maximum_toys(cost, N, K):
    count,total = 0,0

    for c in sorted(cost):
        if total + c <= K:
            total += c
            count += 1
        else:
            break

    return count

n = 7
cost = [1, 4, 5, 3, 2, 1, 6]
K = 6
print(maximum_toys(cost, n, K))
