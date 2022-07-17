# https://leetcode.com/problems/populating-next-right-pointers-in-each-node/

from typing import Optional
from collections import deque
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    # traverse level-by-level
    # then connect nodes on the same level
    # time: O(n)  n: number of nodes
    # space: same
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        # special case
        if not root:
            return None

        # level-order traversal is implemented using a FIFO queue
        # element of the queue (node, height of the current node)
        def level_order_traverse(root):
            nonlocal level_order_result
            queue = deque([(root, 0)])
            while queue:
                node, height = queue.popleft()
                level_order_result.append((node, height))
                if node.left:
                    queue.append((node.left, height + 1))
                if node.right:
                    queue.append((node.right, height + 1))

        level_order_result = []
        level_order_traverse(root)

        for i in range(len(level_order_result) - 1):
            # if they are on the same level, connect them
            if level_order_result[i][1] == level_order_result[i + 1][1]:
                level_order_result[i][0].next = level_order_result[i + 1][0]
        return root





