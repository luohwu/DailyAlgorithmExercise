# https://leetcode.com/problems/flood-fill/
from typing import  List
from collections import deque


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        rows,cols=len(image),len(image[0])

        #flag table to record visit
        visit_table=[[0]*cols for i in range(rows)]

        # buffer pixels to be modified
        pixels_to_change=[]

        scolor=image[sr][sc]

        #queue of pixels to visit
        queue=deque([[sr,sc]])
        # up, down,left, right
        possible_move=[[-1,0],[1,0],[0,-1],[0,1]]
        while queue:
            current_r,current_c=queue.pop()
            #flag
            visit_table[current_r][current_c]=1

            #add
            pixels_to_change.append([current_r,current_c])
            # traverse possible movement
            for move in possible_move:
                next_r,next_c=current_r+move[0],current_c+move[1]
                if next_r>=0 and next_r<rows and next_c>=0 and next_c<cols and image[next_r][next_c]==scolor \
                        and visit_table[next_r][next_c]==0 :
                    queue.append([next_r,next_c])
        for pixel in pixels_to_change:
            image[pixel[0]][pixel[1]]=newColor
        return image


if __name__=='__main__':
    print(Solution().floodFill(
        image=[[1, 1, 1], [1, 1, 0], [1, 0, 1]], sr=1, sc=1, newColor=2
    ))

