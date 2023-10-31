# https://practice.geeksforgeeks.org/problems/common-elements1132/1

class Solution:
    def commonElements (self,ar1, ar2, ar3, n1, n2, n3):
        common_elements = []
        i, j, k = 0, 0, 0
        
        while i < n1 and j < n2 and k < n3:
            
            if ar1[i] == ar2[j] == ar3[k]:
                
                if not common_elements or ar1[i] != common_elements[-1]:
                    common_elements.append(ar1[i])
                    
                i += 1
                j += 1
                k += 1
                
            elif min (ar1[i], ar2[j], ar3[k]) == ar1[i]:
                i += 1
            
            elif min (ar1[i], ar2[j], ar3[k]) == ar2[j]:
                j += 1 
            
            else:
                k += 1 
        
        return common_elements
