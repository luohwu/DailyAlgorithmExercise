# https://leetcode.com/problems/recover-binary-search-tree/

from typing import Optional
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:

    # the in_order_traversal of a BST should be ascending
    # this problem is equal to: there are two dis-ordered elements in an ascending order, swap the two elements to make it correct
    # Time: O(n) n:number of nodes
    # Space: same
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def in_order_traverse(node):
            if not node:
                return []
            return in_order_traverse(node.left)+[node]+in_order_traverse(node.right)
        in_order_node=in_order_traverse(node=root)
        node_idx_to_swap=[]

        # find the dis-ordered elements in the in_order_traversal result
        for i in range(len(in_order_node)-1):
            if in_order_node[i].val>in_order_node[i+1].val:
                node_idx_to_swap.append(i)

        # if the two elements are neighboring
        if len(node_idx_to_swap)==1:
            temp=in_order_node[node_idx_to_swap[0]].val
            in_order_node[node_idx_to_swap[0]].val=in_order_node[node_idx_to_swap[0]+1].val
            in_order_node[node_idx_to_swap[0]+1].val=temp
        # if they are not neighboring
        else:
            temp=in_order_node[node_idx_to_swap[0]].val
            in_order_node[node_idx_to_swap[0]].val=in_order_node[node_idx_to_swap[1]+1].val
            in_order_node[node_idx_to_swap[1]+1].val=temp


