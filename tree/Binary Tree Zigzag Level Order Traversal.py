# https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/

from typing import List,Optional
from collections import deque
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # Time complexity: O(n) beats 99.74% other submissions
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        # prepare two deque, one for left-to-right traverse, the other one for right-to-left traverse
        res=[]
        left_to_right=deque([root])
        right_to_left=deque()
        left=True
        while left_to_right or right_to_left:
            if left:
                # just iterate all elements in the queue
                buffer=[]
                while left_to_right:
                    node = left_to_right.popleft()
                    buffer.append(node.val)
                    if node.left:
                        right_to_left.append(node.left)
                    if node.right:
                        right_to_left.append(node.right)
                left=False
                # buffer is the traverse result of the current layer
                # add the result to global resutl 'res'
                res.append(buffer)
            else:
                # same as left_to_right traverse
                buffer=[]
                while right_to_left:
                    node=right_to_left.pop()
                    buffer.append(node.val)
                    if node.right:
                        left_to_right.appendleft(node.right)
                    if node.left:
                        left_to_right.appendleft(node.left)
                left=True
                res.append(buffer)
        return res




