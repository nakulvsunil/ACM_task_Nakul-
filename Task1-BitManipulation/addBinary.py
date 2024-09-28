class Solution(object):
    def addBinary(self, a, b):
        L=[]#List to store the added values
        carry = 0 #Carry variable
        i,j=len(a)-1,len(b)-1
        while i>=0 or j>=0 or carry:
            Abit=int(a[i]) if i>=0 else 0 # If the bit is exhausted then take 0
            Bbit=int(b[j]) if j>=0 else 0# If the bit is exhausted then take 0

            total=Abit+Bbit+carry#Adding the bits + carry
            L.append(str(total%2))#To make the bit 0 or 1 
            carry=total//2 # Updating carry
            i-=1
            j-=1
        return "".join(L[::-1])#Returning the result

        
            


        
