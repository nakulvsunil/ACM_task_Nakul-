class Solution(object):
    def hammingWeight(self, n):
        nBin=bin(n)[2:].zfill(32)#Taking the binary value and removing prefix
        Set=0 #Counter
        for i in nBin:
            if i=='1':#If bit is equal to 1 increment Set by 1
                Set+=1
        return Set #return the counter

        
