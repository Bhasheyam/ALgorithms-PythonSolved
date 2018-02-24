'''
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like (ie, buy one and sell one share of the stock multiple times). However, you may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).

Seen this question in a real interview bef'''

'''
example
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
        if len(prices) < 2:
            return 0
        i = len(prices) - 1
        ans = 0
        greater = prices[ i ]
        while i >= 0:
            if prices[i] >= greater:
                greater = prices[ i ]
            else:
                ans += greater - prices[i]
                greater = prices[i]
            i -= 1 
        return ans