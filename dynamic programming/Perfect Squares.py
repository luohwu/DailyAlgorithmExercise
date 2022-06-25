# https://leetcode.com/problems/perfect-squares/

class Solution:

    # Time: >O(n) but <O(n^2)
    # Space: O(n) beats 89%
    def numSquares(self, n: int) -> int:
        # first buffer all squares that are less than n
        squares = []
        for i in range(1, n):
            temp = i * i
            if temp <= n:
                squares.append(temp)
            else:
                break
        # we use dp[0...i-1] to compute dp[i]
        # dp[i] means the least number of squares that sum up to i
        # specially dp[1]=1
        dp = [10 ** 5] * (n + 1)
        dp[1] = 1

        for i in range(1, n + 1):
            # if i is a square number , dp[i]=1
            if i in squares:
                dp[i] = 1
            else:

                # check different combinations
                for square in squares:
                    if square < i:
                        dp[i] = min(dp[i - square] + 1, dp[i])
                    else:
                        break

        return dp[-1]



if __name__=='__main__':
    print(Solution().numSquares(
        n=12
    ))
