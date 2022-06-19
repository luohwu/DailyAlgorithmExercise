# https://leetcode.com/problems/palindrome-partitioning/


from typing import List

class Solution:
    # first we apply dynamic programming to compute a dp_table[left][right]
    # s[left:right+1] is a palindrome only if dp_table[left][right]==True

    # Having the dp_table ready,
    # the rest is just a DFS
    def partition(self, s: str) -> List[List[str]]:
        def search(last_end,path):

            # reach one partition solution
            if last_end==n-1:

                # decode the contect using the partition points in 'path'

                temp=[]
                start=0
                for index in path:
                    temp.append(s[start:index+1])
                    start=index+1
                res.append(temp)

            # check if there is a palindrome partition in the rest of the string
            new_start=last_end+1
            for new_end in range(new_start,n):
                if dp_table[new_start][new_end]==True:
                    search(new_end,path+[new_end])


        n=len(s)
        dp_table=[[False]*n for i in range(n)]

        # 'e', 'f','e' in 'efe' is palindrome
        for i in range(n):
            dp_table[i][i]=True

        # star dp to check if any substring s[left:right] is palindrome
        for i in range(n-2,-1,-1):
            left=i
            right=i+1
            while right<n:
                if right-left==1:
                    if s[left]==s[right]:
                        dp_table[left][right]=True
                else:
                    if dp_table[left+1][right-1] and s[left]==s[right]:
                        dp_table[left][right]=True
                    else:
                        dp_table[left][right]=False
                right+=1

        # start searching using the computed dp_table
        res=[]

        search(-1,[]) # initially, the path is empty, the last_end index is -1, which means the new_start is 0

        return res

if __name__=='__main__':
    print(Solution().partition(
        'efe'
    ))


