# https://leetcode.com/problems/valid-anagram/
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counts_s=[0]*26
        counts_t=[0]*26
        for char in s:
            counts_s[ord(char) - ord('a')] += 1
        for char in t:
            counts_t[ord(char) - ord('a')] += 1
        for i in range(26):
            if counts_s[i]!=counts_t[i]:
                return False
        return True

if __name__=='__main__':
    print(Solution().isAnagram(
        "anagram",
        "nagaram"
    ))