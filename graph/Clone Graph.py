
# https://leetcode.com/problems/clone-graph/

from collections import deque

class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []



class Solution:
    def bfs(self,node:'Node'):
        to_copy=deque([node]) # nodes to be visited
        copied={node:Node(val=node.val)}
        while to_copy:
            cur_node=to_copy.popleft()
            for neighbor in cur_node.neighbors:
                if neighbor not in copied:
                    copied[neighbor]=Node(val=neighbor.val)
                    to_copy.append(neighbor)
                copied[cur_node].neighbors.append(copied[neighbor])
        return copied[node]

    def dfs(self,node:'Node'):
        to_copy=deque([node]) # nodes to be visited
        copied={node:Node(val=node.val)}
        while to_copy:
            cur_node=to_copy.pop()
            for neighbor in cur_node.neighbors:
                if neighbor not in copied:
                    copied[neighbor]=Node(val=neighbor.val)
                    to_copy.append(neighbor)
                copied[cur_node].neighbors.append(copied[neighbor])
        return copied[node]



    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None
        return self.bfs(node)

