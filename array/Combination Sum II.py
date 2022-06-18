# https://leetcode.com/problems/combination-sum-ii/

from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def search(nums, target, path):
            if sum(nums) < target:
                return
            if target == 0:
                if path not in res:
                    res.append(path)
            if target < 0:
                return
            for idx, num in enumerate(nums):
                new_path = path + [num]
                if new_path not in path_buffer:
                    path_buffer.append(new_path)
                    search(nums[idx + 1:], target - num, new_path)

        candidates.sort()
        res = []
        # for some special cases,
        # we need this buffer to avoid more redundant computation
        path_buffer = []
        search(candidates, target, [])
        return res

if __name__=='__main__':
    print(Solution().combinationSum2(
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    27
    ))

