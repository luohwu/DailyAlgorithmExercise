# https://leetcode.com/problems/most-frequent-subtree-sum/

from typing import Optional,List
from collections import defaultdict

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    # recursive traversal from bottom to up
    # subtree_sum(node)=node.val+subtree_sum(node.left)+subtree_sum(node.right)
    # use a dict to store all found subtree_sum
    # sort according to frequency
    # pick the most frequent one(s)
    # Time: O(n), n: #of nodes
    # Space: same
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        def compute_subtree_sum(node:Optional[TreeNode]):
            nonlocal global_dict
            if not node:
                return 0
            else:
                sum_left_subtree=compute_subtree_sum(node.left)
                sum_right_subtree=compute_subtree_sum(node.right)
                sum_cur=sum_left_subtree+sum_right_subtree+node.val
                global_dict[sum_cur]+=1
                return sum_cur

        global_dict=defaultdict(int)
        compute_subtree_sum(root)
        # print(global_dict)
        sorted_dict=sorted(global_dict.items(),key=lambda item:-item[1])
        res=[]
        # print(sorted_dict)
        max_val=sorted_dict[0][1]
        for key,val in sorted_dict:
            if val==max_val:
                res.append(key)
        return res