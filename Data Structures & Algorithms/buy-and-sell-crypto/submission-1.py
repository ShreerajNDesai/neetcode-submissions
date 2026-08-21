class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mind = prices[0]
        maxp = 0

        for i in prices:
            maxcurr = int(i - mind)
            if i < mind:
                mind = i
            elif maxcurr > maxp:
                maxp = maxcurr
                
                
        return maxp
