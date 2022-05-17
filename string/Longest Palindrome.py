# https://leetcode.com/problems/longest-palindrome/


class Solution:
    def longestPalindrome(self, s: str) -> int:
        table=[0]*58
        start=ord('A')
        for char in s:
            idx=ord(char)-start
            table[idx]+=1
        result=0
        flag=False
        for item in table:
            if item%2==1:
                flag=True
            result+=(item-item%2)
        if flag:
            result+=1
        return result


if __name__=='__main__':
    print(Solution().longestPalindrome(
        "zeusnilemacaronimaisanitratetartinasiaminoracamelinsuez"
    ))
