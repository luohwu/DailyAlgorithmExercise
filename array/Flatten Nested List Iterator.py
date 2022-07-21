# https://leetcode.com/problems/flatten-nested-list-iterator/

from typing import List

class NestedInteger:
   def isInteger(self) -> bool:
       """
       @return True if this NestedInteger holds a single integer, rather than a nested list.
       """

   def getInteger(self) -> int:
       """
       @return the single integer that this NestedInteger holds, if it holds a single integer
       Return None if this NestedInteger holds a nested list
       """

   def getList(self) -> [NestedInteger]:
       """
       @return the nested list that this NestedInteger holds, if it holds a nested list
       Return None if this NestedInteger holds a single integer
       """


class NestedIterator:
    # flatten the NestedInteger in the construction function directly
    # in the flatten process, recursion can be used
    # two cases: a) is Integer b) not an Integer
    def __init__(self, nestedList: [NestedInteger]):
        def decode_nested_list(nestedList: NestedInteger):
            if nestedList.isInteger():
                return [nestedList.getInteger()]
            else:
                res = []
                for list in nestedList.getList():
                    res = res + decode_nested_list(list)
                return res

        self.flatten_list = []
        for item in nestedList:
            self.flatten_list += decode_nested_list(item)
        self.cur_idx = -1
        self.num_items = len(self.flatten_list)

    def next(self) -> int:
        self.cur_idx += 1
        return self.flatten_list[self.cur_idx]

    def hasNext(self) -> bool:
        return self.cur_idx < self.num_items - 1