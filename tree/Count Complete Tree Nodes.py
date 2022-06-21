# https://leetcode.com/problems/count-complete-tree-nodes/

from  typing import Optional
from collections import deque
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # first, visit the most left leaves node first, track the height 'H'
    # ending condition: the height of the current node 'h' satisfies 'h'=='H-1' and there is no children
    # Time complexity: <O(n), beats 99.34% XD!
    # Memory complexity: <O(n) beats 86.08%
    def countNodes(self, root: Optional[TreeNode]) -> int:


        H=-1 # track the highest height
        node_at_H=0 #  number of nodes at H
        queue=deque([(root,0)])
        while queue:
            node,h=queue.pop()
            # corner case
            if not node:
                continue

            # the current node is higher than previous nodes
            if h>H:
                H=h
                node_at_H=1
            # find another leaves node at height H
            elif h==H:
                node_at_H+=1
            # find the termination node
            elif h==H-1 and not node.left and not node.right:
                break
            # print(node.val,H,node_at_H)
            # traverse left first, then right
            queue.append((node.right,h+1))
            queue.append((node.left,h+1))

        # previous_nodes: number of nodes at height 0~H-1
        previous_nodes=0
        for i in range(H):
            previous_nodes+=2**i # can also use a math equation instead of a loop
        return previous_nodes+node_at_H

