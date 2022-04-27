# https://leetcode.com/problems/merge-two-sorted-lists/

from collections import deque
from typing import Optional
from typing import List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 and not list2:
            return None
        if not list1:
            return list2
        if not list2:
            return list1
        if list1.val>list2.val:
            resultHead=list2
            list2=list2.next
        else:
            resultHead=list1
            list1=list1.next
        current_node=resultHead
        while list1 or list2:
            if list1 and list2:
                if list1.val<list2.val:
                    current_node.next=ListNode(val=list1.val,next=None)
                    current_node=current_node.next
                    list1=list1.next
                else:
                    current_node.next=ListNode(val=list2.val,next=None)
                    current_node=current_node.next
                    list2=list2.next
            elif list1:
                current_node.next=ListNode(val=list1.val,next=None)
                current_node=current_node.next
                list1=list1.next
            else:
                current_node.next=ListNode(val=list2.val,next=None)
                current_node=current_node.next
                list2=list2.next
        return resultHead

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        n = len(lists)
        if n == 0:
            return None
        if n == 1:
            return lists[0]
        result = lists[0]
        for item in lists[1:]:
            result = self.mergeTwoLists(result, item)
        return result


