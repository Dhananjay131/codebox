class Solution:
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        return s[::-1]
    #''.join(reversed('a string')) this works as well. 
    # *Strings are immuatable in python. Changing a string does not modify the string. It creates a new one.
