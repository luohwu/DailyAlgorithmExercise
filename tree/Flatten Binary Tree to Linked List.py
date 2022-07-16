# https://leetcode.com/problems/flatten-binary-tree-to-linked-list/
from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    # just simpley pre_order_traverse, then modify node.left and node.right
    # mind the last node, last.right=None
    # Time: O(n), n: number of nodes
    # Space: same
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root :
            return None
        def pre_order_traversal(node):
            if not node:
                return []
            return [node]+pre_order_traversal(node.left)+pre_order_traversal(node.right)
        pre_order_result=pre_order_traversal(root)
        for i in range(len(pre_order_result)-1):
            pre_order_result[i].left=None
            pre_order_result[i].right=pre_order_result[i+1]
        pre_order_result[-1].left = None
        pre_order_result[-1].right = None
        return pre_order_result[0]

