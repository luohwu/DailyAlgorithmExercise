# https://leetcode.com/problems/group-anagrams/

from typing import  List
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        table=dict()
        sorted_strs=[''.join(sorted(s)) for s in strs]
        for idx,s in enumerate(sorted_strs):
            if s not in table.keys():
                table[s]=[strs[idx]]
            else:
                table[s]=table[s]+[strs[idx]]

        return list(table.values())


if __name__=='__main__':
    print(Solution().groupAnagrams(
        strs=["eat", "tea", "tan", "ate", "nat", "bat"]
    ))