class Solution:
    def removeConsecutiveCharacter(self, S):

        modified_str = S[0] 

        for i in range(1, len(S)):
            if S[i] != S[i - 1]: 
                modified_str += S[i]
    
        return modified_str
