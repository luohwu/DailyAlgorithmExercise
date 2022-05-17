# https://leetcode.com/problems/ransom-note/

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        available_char=[0]*26
        start=ord('a')
        for char in magazine:
            available_char[ord(char)-start]+=1
        for char in ransomNote:
            if available_char[ord(char)-start]>0:
                available_char[ord(char)-start]-=1
            else:
                return False
        return True

if __name__=='__main__':
    print(Solution().canConstruct(
        ransomNote="a", magazine="b"
    ))