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

    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
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







if __name__=='__main__':
    print(Solution().findMinHeightTrees(
        n = 6, edges = [[3,0],[3,1],[3,2],[3,4],[5,4]]
    ))
