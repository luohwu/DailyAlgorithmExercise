# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
from typing import Optional,List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import deque


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if len(preorder)==0:
            return None
        #parent node P must be the first element
        # in inorder traverse, all left nodes are on the left side of P
        # all right nodes are on the right side of P
        # find left subtree and right subtree, then recurse
        node=TreeNode(val=preorder[0])
        parent_in_inorder=inorder.index(node.val)
        inorder_left=inorder[0:parent_in_inorder]
        inorder_right=inorder[parent_in_inorder+1:]
        preorder_left=preorder[1:1+len(inorder_left)]
        preorder_right=preorder[1+len(inorder_left):]
        node.left=self.buildTree(preorder_left,inorder_left)
        node.right=self.buildTree(preorder_right,inorder_right)
        return node
