# https://leetcode.com/problems/house-robber-iii/
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # recursion + dynamic programming
    # for a given node 'N',
    # if we rob 'N', we must skip N.left and N.right
    # if we skil 'N', there are 4 possible paths: [rob,rob] [rob, skip], [skip,rob] [skip,skip], pick the best one

    def rob(self, root: Optional[TreeNode]) -> int:
        @cache
        def rob_sub_tree(node:Optional[TreeNode],rob=True):
            if not node:
                return 0
            if rob:
                return node.val+rob_sub_tree(node.left,rob=False)+rob_sub_tree(node.right,rob=False)
            else:
                return max(rob_sub_tree(node.left, rob=True) + rob_sub_tree(node.right, rob=True),
                           rob_sub_tree(node.left, rob=False) + rob_sub_tree(node.right, rob=False),
                           rob_sub_tree(node.left, rob=True) + rob_sub_tree(node.right, rob=False),
                           rob_sub_tree(node.left, rob=False) + rob_sub_tree(node.right, rob=True),)
        return max(rob_sub_tree(root,False),rob_sub_tree(root,True))