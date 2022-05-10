# https://leetcode.com/problems/palindromic-substrings/

class Solution:
    def countSubstrings(self, s: str) -> int:
        n=len(s)
        dp_table=[[False]*n for i in range(n)]
        res=0
        for start in range(n-1,-1,-1):
            for end in range(start,n):
                if s[start]==s[end]:
                    if end-start<=1 or dp_table[start+1][end-1]==True:
                        dp_table[start][end]=True
                        res+=1
                else:
                    dp_table[start][end]=False
        return res

if __name__=='__main__':
    print(Solution().countSubstrings(
        "aaa"
    ))

