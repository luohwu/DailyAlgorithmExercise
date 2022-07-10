# https://leetcode.com/problems/unique-binary-search-trees-ii/


from typing import  List,Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    # different from  https://leetcode.com/problems/unique-binary-search-trees/
    # we start from bottom to up
    # given List 'nums'
    # there are len(nums) kinds of possible root
    # we first compute result of nums[:root_idx] and nums[root_idx+1:]
    # then it's a combination problem
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        def generateTreesFromList(nums:List):

            # stop case
            if not nums:
                return [None]
            l=len(nums)
            temp=[]
            # check all possible choice of root
            for root_idx in range(l):

                # check left and right
                trees_left_child=generateTreesFromList(nums[:root_idx])
                trees_right_child=generateTreesFromList(nums[root_idx+1:])

                # check each combination of new tree
                for left in trees_left_child:
                    for right in trees_right_child:
                        root=TreeNode(val=nums[root_idx],left=left,right=right)
                        temp.append(root)
            return temp
        return generateTreesFromList(list(range(1,n+1)))



