# https://leetcode.com/problems/minimum-absolute-difference-in-bst/

from typing import Optional
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # pre_order traverse
    # then iterate the result
    # Time O(n)
    # Space O(n)
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        def in_order_traverse(root):
            if not root:
                return []
            else:
                return in_order_traverse(root.left)+[root.val]+in_order_traverse(root.right)
        in_order_result=in_order_traverse(root)
        res=10**5
        for i in range(1,len(in_order_result)):
            res=min(res,in_order_result[i]-in_order_result[i-1])
        return res

