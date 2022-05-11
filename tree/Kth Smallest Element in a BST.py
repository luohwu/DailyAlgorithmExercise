# https://leetcode.com/problems/kth-smallest-element-in-a-bst/
from typing import Optional,List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import deque


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def inorder_traverse(root):
            if not root:
                return []
            else:
                return inorder_traverse(root.left)+[root.val]+inorder_traverse(root.right)

        # inorder traverse, then output the k-1 th element
        inorder_result=inorder_traverse(root)
        return inorder_result[k-1]
