class Solution:
    # @param A : tuple of integers
    # @return a list of integers
    def repeatedNumber(self, A):
        n = len(A)
       
        b = n * (n + 1) // 2 - sum(set(A)) #missing
        num_set = set()
        for num in A:
            if num in num_set:
                a = num
                break
            num_set.add(num)


        return [a, b]
