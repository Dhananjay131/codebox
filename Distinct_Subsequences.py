class Solution:
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        len_1=len(s)
        len_2=len(t)

        
        x =[[0]*(len_2+1) for _ in range(len_1+1)]
        
        for i in range(0,len_1+1):
            x[i][0]=1
        
        
        for i in range(len_1):
            for j in range(len_2):
                if s[i]==t[j]:
                    x[i+1][j+1]= x[i][j+1] + x[i][j]
                else:
                    x[i+1][j+1]= x[i][j+1]
        print(x)   
        return x[len_1][len_2]