class Solution:
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        m=len(word1)+1
        n=len(word2)+1

        tbl = {}
        for i in range(m): tbl[i,0]=i
        for j in range(n): tbl[0,j]=j
        for i in range(1, m):
            for j in range(1, n):
                cost = 0 if word1[i-1] == word2[j-1] else 1
                tbl[i,j] = min(tbl[i, j-1]+1, tbl[i-1, j]+1, tbl[i-1, j-1]+cost)
                
        return tbl[i,j]