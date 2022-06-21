# https://leetcode.com/problems/delete-node-in-a-bst/

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        node=root
        while node and node.val!=key:
            if key<node.val:
                node=node.right
            else:
                node=node.left


