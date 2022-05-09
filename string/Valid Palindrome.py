# https://leetcode.com/problems/valid-palindrome/
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        s=list(filter(str.isalnum,s))
        return s==s[::-1]



if __name__=='__main__':
    print(Solution().isPalindrome(
        "anagra m"
    ))