# https://leetcode.com/problems/implement-trie-prefix-tree/
from typing import Optional,List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import deque


class Trie:

    #based on a binary search tree
    # all operations can be done as operations in a search binary tree
    def __init__(self):
        self.root=None

    def insert(self, word: str) -> None:

        #empty case
        if not self.root:
            self.root=TreeNode(val=word,left=None,right=None)
            return

        node=self.root
        while 1:
            # should be added to the right subtree
            if node.val<word:

                #if node.right exist, continue comparing
                if node.right:
                    node=node.right
                # if node.right==None, it is the place to insert
                else:
                    node.right=TreeNode(val=word)
                    break
            elif node.val>word:
                if node.left:
                    node=node.left
                else:
                    node.left=TreeNode(val=word)
                    break
            else:
                break

    def search(self, word: str) -> bool:
        node=self.root
        while node:
            # find one
            if node.val==word:
                return True
            #continue in the right direction
            if node.val<word:
                node=node.right
            else:
                node=node.left

        # could not find one
        return False

    def startsWith(self, prefix: str) -> bool:
        #similar to the search operatio
        # just compare the prefix of node.val
        node=self.root
        while node:
            if prefix == node.val[:len(prefix)]:
                return True
            if node.val<prefix:
                node=node.right
            else:
                node=node.left
        return False

# check which one is wrong
# if __name__=='__main__':
#     action=["Trie","insert","insert","insert","insert","insert","insert","search","search",
#     "search","search","search","search","search","search","search","startsWith",
#     "startsWith","startsWith","startsWith","startsWith","startsWith","startsWith"
#     ,"startsWith","startsWith"]
#
#     target=[[],["app"],["apple"],["beer"],["add"],["jam"],["rental"],["apps"],["app"],["ad"],
# ["applepie"],["rest"],["jan"],["rent"],["beer"],["jam"],["apps"],["app"],["ad"],
# ["applepie"],["rest"],["jan"],["rent"],["beer"],["jam"]]
#
#     result=[None,None,None,None,None,None,None,False,True,False,False,False,False,False,False,False,False,True,False,False,False,False,True,False,False]
#
#     for i in range(len(action)):
#         print(action[i],target[i],result[i])

