# https://leetcode.com/problems/sum-of-left-leaves/

from typing import Optional
from collections import deque
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    # Time: O(n)
    # Space: O(1)
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        queue=deque([root])
        res=0
        while queue:
            node=queue.popleft()
            if not node:
                continue
            # find a left leaf node
            if node.left and not node.left.left and not node.left.right:
                res+=node.left.val
            else:
                # normal left node
                queue.append(node.left)
            # visit right node
            queue.append(node.right)
        return  res
