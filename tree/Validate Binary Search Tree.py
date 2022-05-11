# https://leetcode.com/problems/validate-binary-search-tree/
from typing import Optional,List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import deque


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # inorder traversal
        def inorder_traversal(root):
            if not root:
                return []
            else:
                return inorder_traversal(root.left) + [root.val] + inorder_traversal(root.right)

        inorder_result = inorder_traversal(root)

        # a sort operation wont change the inorder traversal result of valid BST
        # there cant be duplicate value in a vaild BST
        return inorder_result == sorted(inorder_result) and len(inorder_result) == len(set(inorder_result))



