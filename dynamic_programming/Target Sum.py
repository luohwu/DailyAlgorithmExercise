# https://leetcode.com/problems/target-sum/

from typing import List


class Solution:
    # convert this problem to a typical knapsack problem
    # a-b+c=target -> a+c=target+b= 1/2 * sum([a,b,c]+[target])
    # Time: O(n * p) with n=len([a,b,c]) p=1/2 * sum([a,b,c]+[target])
    # Space: same

    # mind the 0s in nums, they can double the answer
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # corner case:
        # no solution
        abs_nums=[abs(item) for item in nums]
        if sum(abs_nums)<target or -sum(abs_nums)>target:
            return 0

        # count number of 0s
        # and remove 0s for converting the original problem to a typical knapsack problem
        nums_of_zeros = sum([1 for num in nums if num == 0])
        nums=[item for item in nums if item != 0]
        all_sum=sum(nums+[target])
        if all_sum%2==1:
            return 0
        converted_target=all_sum//2
        len_of_nums=len(nums)
        # from here, it is a knapsack problem
        dp=[[0]*(converted_target+1) for i in range(len_of_nums+1)]
        dp[0][0]=1
        for col in range(1,converted_target+1):
            dp[0][col]=0
        for row in range(1,len_of_nums+1):
            dp[row][0]=1

        for row in range(1,len_of_nums+1):
            for col in range(1,converted_target+1):
                dp[row][col]=dp[row-1][col]
                if nums[row-1]<=converted_target:
                    dp[row][col]+=dp[row-1][col-nums[row-1]]

        return dp[-1][-1]*(2**nums_of_zeros)




if __name__=='__main__':
    print(Solution().findTargetSumWays(

        [100],
        - 200
    ))