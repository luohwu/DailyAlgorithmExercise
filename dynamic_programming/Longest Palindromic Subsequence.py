# https://leetcode.com/problems/longest-palindromic-subsequence/


class Solution:
    # recursion method is not fast enough
    def longestPalindromeSubseqRE(self, s: str) -> int:
        def search(s):
            if not s:
                return 0
            if len(s)==1:
                return 1
            left=0
            right=len(s)-1

            if s[left]==s[right]:
                return 2+search(s[left+1:right])
            else:
                return max(search(s[left:right]),search(s[left+1:]),search(s[left+1:right]))
        return search(s)

    # DP, dp[i][j] is the solution of longestPalindromeSubseq(s[i:j+1])
    # Time: O(n^2)
    # Space: same
    def longestPalindromeSubseq(self, s: str) -> int:
        n=len(s)
        dp=[[0]*n for i in range(n)]
        for i in range(n-1,-1,-1):
            dp[i][i]=1
            for j in range(i+1,n):
                if s[i]==s[j]:
                    dp[i][j]=2+dp[i+1][j-1]
                else:
                    dp[i][j]=max(dp[i+1][j],dp[i][j-1])
        return dp[0][-1]

if __name__=='__main__':
    print(Solution().longestPalindromeSubseq(
        "aabaaba"
    ))