# https://leetcode.com/problems/climbing-stairs/
# You are climbing a staircase. It takes n steps to reach the top.
# Each time you can either climb 1 or 2 steps.
# In how many distinct ways can you climb to the top?


class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 0 or n == 1:
            return 1
        one = [0] * (n + 1)
        two = [0] * (n + 1)
        one[1] = 1
        two[1] = 0
        one[2] = 1
        two[2] = 1

        for i in range(3, n + 1):
            one[i] = one[i - 1] + two[i - 1]
            two[i] = one[i - 2] + two[i - 2]
        return one[n] + two[n]
