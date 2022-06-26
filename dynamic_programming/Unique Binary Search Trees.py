# https://leetcode.com/problems/unique-binary-search-trees/

class Solution:
    # dp[i] is the solution of numTrees(i)
    # for a given number 'n', check how many root nodes can be choosed
    # for each choice, the number of possible Trees = dp[number_of_left_children]*dp[number_of_right_children]
    # Time: O(n)<x<O(n^2)
    # Space: O(n)
    def numTrees(self, n: int) -> int:
        # initialization
        dp=[0]*(n+1)
        dp[0]=1
        dp[1]=1

        # start dp
        for i in range(2,n+1):
            for root in range(1,i+1):
                number_left_nodes=root-1
                number_right_nodes=i-root
                dp[i]+=(1*dp[number_left_nodes]*dp[number_right_nodes])
        return dp[-1]

if __name__=='__main__':
    print(Solution().numTrees(
        3
    ))