# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/
from typing import Optional,List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import deque

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def preorder_tranverse(root):
            if not root:
                return []
            else:
                return [root.val]+preorder_tranverse(root.left)+preorder_tranverse(root.right)

        preorder_result=preorder_tranverse(root)
        queue=deque([root])
        while queue:
            node=queue.pop()
            if node.left and node.right:
                # values of the left subtree
                val_left_subtree=preorder_result[preorder_result.index(node.val)+1:preorder_result.index(node.right.val)]
                # values of the right subtree
                val_right_subtree=preorder_result[preorder_result.index(node.right.val):]

                # if p and q are in two different subtrees
                if (p.val in val_left_subtree and q.val in val_right_subtree) or \
                    (q.val in val_left_subtree and p.val in val_right_subtree):
                    return node

            # if current value is p's value or q's value
            if node.val == p.val and q.val in preorder_result[preorder_result.index(node.val):]:
                return node
            if node.val == q.val and p.val in preorder_result[preorder_result.index(node.val):]:
                return node
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)


