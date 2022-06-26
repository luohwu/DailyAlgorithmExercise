from typing import List
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        res = [99999] * (amount + 1)
        res[0] = 0
        if 1 in coins:
            res[1] = 1
        for cur_amount in range(2, amount + 1):
            for coin in coins:
                if cur_amount-coin>0:
                    if res[cur_amount] > res[cur_amount - coin] + 1:
                        res[cur_amount] = res[cur_amount - coin] + 1
        print(res)
        result = -1 if res[amount] == 99999 else res[amount]
        return result
if __name__=='__main__':
    solution=Solution().coinChange(coins=[1,2,5],amount=11)
    print(solution)

