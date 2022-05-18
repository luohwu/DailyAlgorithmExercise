# https://leetcode.com/problems/diameter-of-binary-tree/

# Definition for a binary tree node.
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter=0

        #compute height the current tree
        def compute_height(node):
            if not node:
                return 0
            height_left=compute_height(node.left)
            height_right=compute_height(node.right)
            nonlocal diameter
            # diameter of the current tree is height_left+height_right
            # then compare with max value
            if height_right+height_left>diameter:
                diameter=height_right+height_left
            return 1+max(height_right,height_left)
        compute_height(root)
        return diameter

