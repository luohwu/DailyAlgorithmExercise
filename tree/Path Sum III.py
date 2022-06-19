# https://leetcode.com/problems/path-sum-iii/

from typing import Optional,List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:

        # check each path
        # assume the old path is [a,b], and trajectory=[0, 0+ a.val, 0+a.val+b.val]
        # given the new node c, the sum of the current path is : 0+a+b+c
        # child-path b->c = (0+a+b+c)-(0+a)= new_sum-trajectory[1]
        # if sum(b->c)==targetSum, record the path
        def search(node: Optional[TreeNode], trajectory: List):
            nonlocal res
            # None node
            if not node:
                return
            new_sum = trajectory[-1] + node.val
            # check the path from each node in the trajectory to the current node
            for item in trajectory:
                if new_sum - item == targetSum:
                    res += 1

            # move further
            new_trajectory = trajectory + [new_sum]
            search(node.left, new_trajectory)
            search(node.right, new_trajectory)

        res = 0
        search(root, [0])
        return res


