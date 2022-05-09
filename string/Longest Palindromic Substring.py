# https://leetcode.com/problems/longest-palindromic-substring/
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n=len(s)
        dp_table=[[False]*n for i in range(n)]
        for i in range(n):
            dp_table[i][i]=True
        for start in range(n-1,-1,-1):
            for end in range(start+1,n):
                if s[start]==s[end]:
                    if end-start<=1 or dp_table[start+1][end-1]:
                        dp_table[start][end]=True
        res=""
        max_length=0
        for start in range(n):
            for end in range(start,n):
                if dp_table[start][end] and end-start+1>max_length:
                    max_length=end-start+1
                    res=s[start:end+1]
        return res



if __name__=='__main__':
    print(Solution().longestPalindrome(
        "cbbd"
    ))