class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        pars = [None]   #think Y
        parmap = {')': '(', '}': '{', ']': '['}
        for c in s:
            if c in parmap and parmap[c] == pars[len(pars)-1]:    #bcz this len-1 gives index error
                pars.pop()
            else:
                pars.append(c)
        return len(pars) == 1
