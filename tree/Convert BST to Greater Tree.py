# https://leetcode.com/problems/convert-bst-to-greater-tree/

from typing import List,Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def in_order_traverse(root):
            if not root:
                return []
            return in_order_traverse(root.left)+[root.val]+in_order_traverse(root.right)

        def convert(root):
            if not root:
                return
            nonlocal in_order_result
            index=in_order_result.index(root.val)
            root.val+=sum(in_order_result[index+1:])
            convert(root.left)
            convert(root.right)

        in_order_result=in_order_traverse(root)
        convert(root)
        return root
