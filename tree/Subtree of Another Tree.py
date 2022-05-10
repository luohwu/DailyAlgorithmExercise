# https://leetcode.com/problems/subtree-of-another-tree/
from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import deque
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def equal(root1,root2):
            if not root1 and not root2:
                return True
            if (root1 and not root2) or (not root1 and root2):
                return False
            if root1.val!=root2.val:
                return False
            return equal(root1.left,root2.left) and equal(root1.right,root2.right)
        queue=deque([root])
        while(queue):
            node=queue.pop()
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
            if equal(node,subRoot):
                return True
        return False


