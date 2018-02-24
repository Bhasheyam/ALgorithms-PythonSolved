'''
Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (ie, buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Example 1:
Input: [7, 1, 5, 3, 6, 4]
Output: 5

max. difference = 6-1 = 5 (not 7-1 = 6, as selling price needs to be larger than buying price)

'''




class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        i = len(prices) - 1
        ans = 0
        greater = prices[ i ]
        while i >= 0:
            if prices[i] >= greater:
                greater = prices[ i ]
            else:
                ans = max(ans,(greater - prices[i]))
            i -= 1 
        return ans

s =Solution() 
prices = [7,1,5,3,6,4]
print s.maxProfit(prices)