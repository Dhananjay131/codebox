class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        a = b = 1
        for _ in range(n):
            a, b = b, a + b
        return a
        #kinda fibonacci, right and check pattern