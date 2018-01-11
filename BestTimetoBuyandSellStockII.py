class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if prices == []:
            return 0
        else:
            totalprofit = 0
            for i in range(1,len(prices)):
                if (prices[i] > prices[i-1]):
                    totalprofit += prices[i] - prices[i-1]
            return totalprofit
