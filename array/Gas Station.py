# https://leetcode.com/problems/gas-station/
from typing import List


class Solution:

    # time complexity: O(n)
    # space complexity: O(n) beat 99.37% submissions, can be optimized to O(1) by modifying the input gas or cost
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:

        # net array, for simpler processing
        n = len(gas)
        net=[0]*n
        for i in range(n):
            net[i]=gas[i]-cost[i]

        # next means the next position to try, to skip redundant iterations
        # this can be updated during traversing
        next=0
        for i in range(n):
            if i<next:
                continue

            # temp net value
            temp=0
            idx=i
            # as long as there is still gas left (>=0)
            while temp >= 0:
                temp+=net[idx]

                # move toward the next gas station
                # the edge case
                if idx==n-1:
                    idx=0
                else:
                    idx+=1
                # success
                if idx==i:
                    if temp>=0:
                        return i
            next=idx
        return -1


if __name__=='__main__':
    print(Solution().canCompleteCircuit(

        gas=[2, 3, 4], cost=[3, 4, 3]

    ))


