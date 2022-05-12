# # https://leetcode.com/problems/design-add-and-search-words-data-structure/
#
# from typing import Optional,List
# # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#
# from collections import deque
#
#
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#
# from collections import deque
#
#
# class WordDictionary:
#
#     #based on a binary search tree
#     # all operations can be done as operations in a search binary tree
#     def __init__(self):
#         self.root=None
#
#     def addWord(self, word: str) -> None:
#
#         #empty case
#         if not self.root:
#             self.root=TreeNode(val=word,left=None,right=None)
#             return
#
#         node=self.root
#         while 1:
#             # should be added to the right subtree
#             if node.val<word:
#
#                 #if node.right exist, continue comparing
#                 if node.right:
#                     node=node.right
#                 # if node.right==None, it is the place to insert
#                 else:
#                     node.right=TreeNode(val=word)
#                     break
#             elif node.val>word:
#                 if node.left:
#                     node=node.left
#                 else:
#                     node.left=TreeNode(val=word)
#                     break
#             else:
#                 break
#
#     def search(self, word: str) -> bool:
#         length_word=len(word)
#         node=self.root
#         if '.' not in word:
#             while(node):
#                 if node.val<word:
#                     node=node.right
#                 elif node.val>word:
#                     node=node.left
#                 else:
#                     return True
#             return False
#         else:
#             index_first_dot=word.index('.')
#             pred_word=word[:index_first_dot]
#             if index_first_dot > 0:
#                 while (len(node.val) > 1 + index_first_dot):
#                     if node.val > pred_word:
#                         node = node.left
#                     elif node.val<pred_word:
#                         node = node.right
#                     else:
#                         break
#             queue = deque([node])
#             while(queue):
#                 node=queue.pop()
#                 if not node:
#                     continue
#                 if len(node.val)==length_word:
#                     point_wise_result = [node.val[i] == word[i] or word[i] == '.' for i in range(length_word)]
#                     if False not in point_wise_result:
#                         return True
#                 queue.append(node.left)
#                 queue.append(node.right)
#             return False