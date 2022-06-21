# https://leetcode.com/problems/minimum-depth-of-binary-tree/

from typing import Optional
from collections import deque
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # just a simple layer-level traverse, until a leaf node is found
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        # initial depth is 1
        queue=deque([(root,1)])
        while queue:
            node,height=queue.popleft()
            if not node:
                continue

            # find a leaf node
            # since we are traverse layer by layer
            # this is our target node with minimum depth
            if not node.left and not node.right:
                return height

            #continue traversing
            else:
                queue.append((node.left,height+1))
                queue.append((node.right,height+1))


