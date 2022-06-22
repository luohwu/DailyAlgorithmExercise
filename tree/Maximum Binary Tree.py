# https://leetcode.com/problems/maximum-binary-tree/

from typing import List,Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # simple recursive
    # Time: O(n)
    # Space: O(n)
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None
        maximum=max(nums)
        index=nums.index(maximum)
        root=TreeNode(val=maximum,left=self.constructMaximumBinaryTree(nums[:index]),
                      right=self.constructMaximumBinaryTree(nums[index+1:]))
        return root
