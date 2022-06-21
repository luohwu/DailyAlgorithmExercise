# https://leetcode.com/problems/binary-tree-paths/

from typing import Optional,List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # easy one, just mind the output format
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        def traverse(node, path):
            nonlocal res
            if path == "":
                path = str(node.val)
            else:
                path = path + '->' + str(node.val)
            if not node.left and not node.right:
                res.append(path)

            else:
                if node.left:
                    traverse(node.left, path)
                if node.right:
                    traverse(node.right, path)

        res = []
        traverse(root, "")
        return res