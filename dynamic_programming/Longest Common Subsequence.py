
# https://leetcode.com/problems/longest-common-subsequence/
# 2D DP
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        length_1 = len(text1)
        length_2 = len(text2)
        dp_table = [[0] * (length_1 + 1) for i in range(length_2 + 1)]
        for i in range(length_2):
            for j in range(length_1):
                if text1[j] == text2[i]:
                    dp_table[i + 1][j + 1] = max(dp_table[i][j] + 1,dp_table[i+1][j],dp_table[i][j+1])
                else:
                    dp_table[i + 1][j + 1] = max(dp_table[i+1][j],dp_table[i][j+1])
        return dp_table[-1][-1]


if __name__=='__main__':
    print(Solution().longestCommonSubsequence('abcde','ace'))