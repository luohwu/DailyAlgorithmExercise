# https://leetcode.com/problems/linked-list-cycle-ii/

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # slow but accepted method
    def detectCycleSlow(self, head: Optional[ListNode]) -> Optional[ListNode]:

        buffer = []
        while head:
            # print(head)
            if head in buffer:
                return head
            else:
                buffer.append(head)
                head = head.next
        return None

    #fast method--Floyd's algorithm
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow=head
        fast=head

        # imagine there are 2 persons running on a cycle and start at the same position
        # the slower person runs at 1m/s
        # the faster person runs at 2m/s
        # then they must meet at the start point again
        cycle=False
        while slow and fast and fast.next:
            slow=slow.next
            fast=fast.next.next
            if slow==fast:
                cycle=True
                temp=slow
                break
        if not cycle:
            return None

        # since the two persons start at the head of the link, instead of the start point of the cycle
        # the distance between |head-start| equals to |start-head|
        # just iterate |head-start| times
        while head!=temp:
            head=head.next
            temp=temp.next
        return temp
