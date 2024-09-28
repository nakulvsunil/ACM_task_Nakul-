class Solution(object):
    def singleNumber(self, nums):
        Dict={} #Dictionary to store the number and it's occurence
        for i in nums:
            if i in Dict: # If there in Dict increment value by 1 
                Dict[i]=Dict[i]+1
            else:         #If not there add the key:value pair
                Dict[i]=1
        for key,value in Dict.items():
            if value == 2:#Skipping number if occurence is equal to 2
                continue
            else:        
                return key


            
            
        
