class Solution:
    
    def rob(self, nums):
        last, now = 0, 0
        for k in nums:
            last, now = now, max(last+k,now)
        return(now)
        
        #note: Doo! re-think the trick
