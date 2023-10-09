#https://practice.geeksforgeeks.org/problems/activity-selection-1587115620/1

#Function to find the maximum number of activities that can
    #be performed by a single person.
    def activitySelection(self,n,start,end):
        
        x = []
        
        #pushing the pair of starting and finish day and their 
        #index as pair in another list.
        for i in range(n):
            x.append([[start[i],end[i]],i+1])
        
        #sorting the list.
        x.sort(key=lambda t:(t[0][1],t[0][0]))
        last = 0
        res = 0
        
        for i in range(n) :
            
            #if the starting day of this activity is greater than or equal
            #to the finish day of previously selected day then 
            #we increment the counter and update last.
            if x[i][0][0] > last :
                res += 1
                last = x[i][0][1]
        
        #returning the counter.
        return res
