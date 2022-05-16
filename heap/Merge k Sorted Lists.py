# https://leetcode.com/problems/merge-k-sorted-lists/

# Definition for singly-linked list.
import heapq
from typing import List,Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        for root in lists:
            while root:
                heap.append(root.val)
                root = root.next

        # convert list to heap
        heapq.heapify(heap)
        # print(heap)
        if len(heap) == 0:
            return None
        else:
            root = ListNode(val=heapq.heappop(heap))
            #keep modifying next node
            node = root
            while len(heap) > 0:
                node.next = ListNode(val=heapq.heappop(heap))
                # print(node)
                node = node.next
        return root







