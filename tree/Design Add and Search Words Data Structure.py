# https://leetcode.com/problems/design-add-and-search-words-data-structure/

from typing import Optional,List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import deque


class WordDictionary:

    # based on a binary search tree
    # all operations can be done as operations in a search binary tree
    def __init__(self):
        self.root = {}

    def addWord(self, word: str) -> None:
        node = self.root
        for char in word:
            node = node.setdefault(char, {})

        # this char is an ending of a word only if 'word' in node.keys()
        node['word'] = True

    def search(self, word: str) -> bool:
        def dfs(node, word):
            # print(node,word)

            if len(word) == 0:
                # none to search , and the current char is an ending-char
                return 'word' in node.keys()
            if word[0] == '.':
                #search all children
                return any([dfs(item, word[1:]) for item in node.values() if item != True])
            else:
                #normal situation
                # if match, search children
                if word[0] in node.keys():
                    return dfs(node[word[0]], word[1:])
                # if not match, return False directly
                else:
                    return False

        return dfs(self.root, word)