# https://leetcode.com/problems/binary-tree-level-order-traversal/
from typing import Optional,List
from collections import deque
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # maintain 2 queues
    # slow_queue for the parent-level nodes
    # fast_queue for the child-level nodes
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        slow_queue=deque([root])
        fast_queue=deque()
        res=[]
        while(slow_queue):
            temp=[]
            while(slow_queue):
                node=slow_queue.popleft()
                temp.append(node.val)
                if node.left:
                    fast_queue.append(node.left)
                if node.right:
                    fast_queue.append(node.right)
            res.append(temp)
            slow_queue=fast_queue
            fast_queue=deque()
        return res