class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        res = "1"
        for i in range(n-1):
            res = self.solve(res)
        return res
            
    def solve(self, s):
        lastSeen = s[0]
        count = 1
        res = ""
        for c in s[1:]:
            if c == lastSeen:
                count += 1
            else:
                res += str(count) + lastSeen
                lastSeen = c
                count = 1
        res += str(count) + lastSeen
        return res
