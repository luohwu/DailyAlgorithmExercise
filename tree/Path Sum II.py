# https://leetcode.com/problems/path-sum-ii/

from typing import List,Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # straightforward: dfs to each leaves node, check sum==target sum
    # note: use new_sum=old_sum+node.val to compute the value of sum, instead of using sum() multiple times
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        def search(node,current_sum,path):
            if not node:
                return
            new_sum=current_sum+node.val
            new_path=path+[node.val]
            if node.left or node.right:
                search(node.left,new_sum,new_path)
                search(node.right,new_sum,new_path)
            else:
                if new_sum==targetSum:
                    res.append(new_path)

        res=[]
        search(root,0,[])
        return res

if __name__=='__main__':
    print(Solution().pathSum(

    ))

