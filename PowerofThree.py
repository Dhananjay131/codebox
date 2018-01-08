class Solution:
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n<1:
            return False
        
        while(n!=1):
            if n % 3 == 0:
                n //=3
                continue
            else:
                return False
            
            
            
        if n==1:
            return True
        
        #return n >0 and 3486784401 % n == 0
