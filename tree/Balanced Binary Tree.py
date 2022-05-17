# https://leetcode.com/problems/balanced-binary-tree/

from typing import Optional
from collections import deque
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # pre-order traverse first
        # then compare the number of elements in the left sub-tree and the right sub-tree
        height_table=dict()
        res=True
        def compute_height(node):
            nonlocal res

            # hight of None is 0
            if not node:
                return 0
            else:
                #left height
                left=compute_height(node.left)
                #right hight
                right=compute_height(node.right)

                #un-balanced situation
                if left-right>1 or right-left>1:
                    res=False

                # height of the current node is 1+ max(children's heights)
                return 1+max(left,right)
        compute_height(root)
        return res
