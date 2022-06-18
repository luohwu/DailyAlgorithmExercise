# https://leetcode.com/problems/combination-sum-iii/
from typing import  List


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:

        # helper function to search the rest elements
        def search(num, target, path):
            if target == num and len(path) == k:
                return res.append(path)
            if target < num:
                return
            for i in range(num + 1, 10):
                search(i, target - num, path + [i])

        res = []

        for i in range(1, 10):
            search(i, n, [i])
        return res

if __name__=='__main__':
    print(Solution().combinationSum3(
        3,7
    ))

