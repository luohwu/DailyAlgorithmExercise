# https://leetcode.com/problems/minimum-height-trees/
from typing import List
from collections import defaultdict


class Solution:
    def findMinHeightTreesSlow(self, n: int, edges: List[List[int]]) -> List[int]:
        def search(start):
            nonlocal table
            nonlocal visit
            visit[start]=True
            if len(table[start])==0:
                return 0
            else:
                return 1+max([0]+[search(child) for child in table[start] if visit[child]==False])
        table=defaultdict(list)

        for start,end in edges:
            table[start].append(end)
            table[end].append(start)
        height=[0]*n
        for i in range(n):
            visit = [False] * n
            height[i]=search(i)-1
        min_height=min(height)
        result=[i for i in range(n) if height[i]==min_height]
        return result

    # faster than the findMinHeightTreesSlow,
    # but still exceed time limit
    def findMinHeightTreesSlow2(self, n: int, edges: List[List[int]]) -> List[int]:
        def search(start):
            self.visit[start]=True
            height_child=[0]
            for child in self.table[start]:
                if self.visit[child]==False:
                    if self.height_table[start][child]==999:
                        self.height_table[start][child]=search(child)
                        height_child.append(self.height_table[start][child])
                    height_child.append(self.height_table[start][child])

            return 1+max(height_child)


        self.height_table=[[999]*n for i in range(n)]
        self.table=defaultdict(list)

        for start,end in edges:
            self.table[start].append(end)
            self.table[end].append(start)
        height=[0]*n
        for i in range(n):
            self.visit = [False] * n
            height[i]=search(i)-1
        # print(height)
        min_height=min(height)
        result=[i for i in range(n) if height[i]==min_height]
        return result

    # think about it twice,
    # the MinHeightTree must be the mid points of the longest path of the given tree
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n==1:
            return [0]
        tree=defaultdict(list)
        for edge in edges:
            p1,p2=edge
            tree[p1].append(p2)
            tree[p2].append(p1)


        leaves=[node for node in tree.keys() if len(tree[node])==1]


        # while there are more than 2 points in the tree
        # keep removing leave ndoes
        while len(tree)>2:
            # print(leaves)
            for leave in leaves:
                par=tree.pop(leave)
                # update the eage of the tree
                tree[par[0]].remove(leave)
            leaves=[node for node in tree.keys() if len(tree[node])==1]
        return list(tree.keys())





if __name__=='__main__':
    print(Solution().findMinHeightTrees(
        6,
        [[0, 1], [0, 2], [0, 3], [3, 4], [4, 5]]
    ))
