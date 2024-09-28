class Solution(object):
    def rangeBitwiseAnd(self, left, right):
        shift=0
        while left<right:
            left>>=1 # We right shift the binary of left until left is equal to right
            right>>=1# We right shift the binary of right until left is equal to left
            shift+=1 #Shift counter
        return left<< shift # Now we left shift the left=right value which will give us bitwise AND of number in range [left,right]
        
