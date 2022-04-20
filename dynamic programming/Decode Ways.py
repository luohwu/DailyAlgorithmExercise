# https://leetcode.com/problems/decode-ways/
from typing import List


class Solution:
    def numDecodings(self, s: str) -> int:

        if s[0] == '0':
            return 0

        table = [str(i) for i in range(1, 27)]
        length = len(s)
        if length == 1:
            return 1
        dp = [0] * (length + 1)
        dp[0] = 1
        dp[1] = 1

        for i in range(1, length):
            last_word = s[i - 1:i + 1]
            if last_word in table:
                if s[i] == '0':
                    dp[i + 1] = dp[i - 1]
                else:
                    dp[i + 1] = dp[i] + dp[i - 1]
            else:
                if s[i] == '0':
                    return 0
                dp[i + 1] = dp[i]
        return dp[-1]


if __name__=='__main__':
    print(Solution().numDecodings("12"))