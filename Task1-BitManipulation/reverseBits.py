class Solution:
    
    def reverseBits(self, n):
        binStr=bin(n)[2:].zfill(32)#We take the binary of n and remove the prefix
        rStr=int(binStr[::-1],2) # Reversing the bits and converting to integer
        
        return rStr




        
