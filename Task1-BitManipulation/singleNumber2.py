class Solution(object):
    def singleNumber(self, nums):
        Dict={}#Dictionary to store the number and it's occurence
        for i in nums:
            if i in Dict: # If there in Dict increment value by 1
                Dict[i]=Dict[i]+1
            else:
                Dict[i]=1
        for key,value in Dict.items():
            if value != 3: #Skipping number if occurence is equal to 3
                return key
               

            
            
        
