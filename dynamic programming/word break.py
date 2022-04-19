# https://leetcode.com/problems/word-break/
from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        length_string = len(s)
        length_dict = len(wordDict)
        dp_table = [False] * length_string

        for i in range(length_string):
            for word in wordDict:
                start_idx = max(0, i - len(word) + 1)
                end_idx = i
                word = s[start_idx:end_idx + 1]
                if word in wordDict:
                    if start_idx == 0:
                        dp_table[i] = True
                    elif dp_table[start_idx - 1] == True:
                        dp_table[i] = True
        return dp_table[-1]


if __name__=='__main__':
    print(Solution().wordBreak("catskicatcats",["cats","cat","dog","ski"]))