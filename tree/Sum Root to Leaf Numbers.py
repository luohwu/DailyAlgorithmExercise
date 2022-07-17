# https://leetcode.com/problems/sum-root-to-leaf-numbers/

from typing import Optional
from collections import deque
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # both DFS and BFS can work

    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        res=0
        queue=deque([(root,str(root.val))])
        while queue:
            node,number=queue.pop()
            if node.right:
                queue.append((node.right,number+str(node.right.val)))
            if node.left:
                queue.append((node.left,number+str(node.left.val)))

            # left node
            if not node.left and not node.right:
                res+=int(number)
        return res
