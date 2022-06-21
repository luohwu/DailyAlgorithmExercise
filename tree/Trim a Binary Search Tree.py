# https://leetcode.com/problems/trim-a-binary-search-tree/
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # recursive method: if the current node is in [low,high], just trim node.left and node.right
    # if node.val>high, the only feasible path is node.left
    # if node.val<low, the only feasible path is node.right
    # Time: <O(n) beats 97.51%
    # Space:O(1)
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        if not root:
            return None

        # feasible situtation, just trim node.left and node.right
        if root.val>=low and root.val<=high:
            root.left = self.trimBST(root.left,low,high)
            root.right = self.trimBST(root.right,low,high)
            return root
        # check node.right
        elif root.val<low:
            return self.trimBST(root.right,low,high)

        # check node.left
        else:
            return self.trimBST(root.left,low,high)


