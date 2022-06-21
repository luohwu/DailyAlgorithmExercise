# https://leetcode.com/problems/find-bottom-left-tree-value/

from typing import Optional
from collections import deque
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    # level order traverse from left to right
    # track the max depth
    # time:  O(n)
    # Space: O(n)
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        max_height=-1
        res=-1
        queue=deque([(root,0)]) #(node, depth)
        while queue:
            node,height=queue.popleft()
            if not node:
                continue
            # find a deeper node, record the value
            if height>max_height:
                max_height=height
                res=node.val
            # normal traverse from left to right
            queue.append((node.left,height+1))
            queue.append((node.right,height+1))
        return  res

