# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/

from typing import List

class Solution:
    # O(N) time
    # O(1) memory beat 99.75 % submissions
    # buy only if there is profit price[i]<price[i+1], hold the share until the next sell point
    # sell once there is profit price[i]>price[i+1]
    def maxProfit(self, prices: List[int]) -> int:
        profit=0
        n=len(prices)
        buy=None
        for idx in range(n-1):
            # no share in hand
            if buy==None:
                # buy if there is profit in the future
                if prices[idx]<prices[idx+1]:
                    buy=prices[idx]

            # with a share in hand
            else:
                # sell once price[idx+1]<price[idx]
                # buy the share back at idx+1
                if prices[idx]>prices[idx+1]:
                    profit+=(prices[idx]-buy)
                    buy=None

        if buy!=None and prices[n-1]>buy:
            profit+=(prices[n-1]-buy)
        return profit


if __name__=='__main__':
    print(Solution().maxProfit(
        prices = [7,6,4,3,1]
    ))

