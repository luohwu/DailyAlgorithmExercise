# https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n=len(s)
        if n==0:
            return 0
        longest_set=dict()
        longest_set[0]=set(s[0])
        for idx,char in enumerate(s[1:],start=1):
            if char not in longest_set[idx-1]:
                longest_set[idx]=longest_set[idx-1].union([char])
            else:
                longest_set[idx]=set([char])
                pre_idx=idx-1
                while pre_idx>-1 and s[pre_idx] not in longest_set[idx]:
                    longest_set[idx].add(s[pre_idx])
                    pre_idx-=1
        length=[len(item) for item in longest_set.values()]
        return max(length)


if __name__=='__main__':
    print(Solution().lengthOfLongestSubstring('qwwek'))