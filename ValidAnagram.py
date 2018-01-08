class Solution:
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        letters = list('abcdefghijklmnopqrstuvwxyz')
        for l in letters:
            if s.count(l) != t.count(l):
                return False
        return True
