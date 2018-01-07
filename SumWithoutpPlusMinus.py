import math
class Solution:
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        
        if max(abs(a),abs(b))> 2147483647:
            return -1
        ta = math.exp(a)
        tb = math.exp(b)
        ta *= tb
        
        res = int(math.log(ta))
        return res
        
