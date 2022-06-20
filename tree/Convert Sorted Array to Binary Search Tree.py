# https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/
from typing import List,Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



class Solution:
    # recursive method
    # each time, pick the mid element as node,   all items on the left are left-subtree, the same to right items
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        left=0
        right=len(nums)
        if right==0:
            return None
        mid=(left+right)//2
        node=TreeNode(val=nums[mid],left=self.sortedArrayToBST(nums[0:mid]),right=self.sortedArrayToBST(nums[mid+1:]))
        return node


