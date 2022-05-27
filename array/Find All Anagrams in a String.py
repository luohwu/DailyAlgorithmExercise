# https://leetcode.com/problems/find-all-anagrams-in-a-string/

from typing import List
from collections import defaultdict
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:

        # record the occurance of each element in p
        target_dict=defaultdict(int)
        for char in p:
            target_dict[char]+=1
        m=len(s)
        n=len(p)
        result=[]
        if m<n:
            return []

        # sliding window
        # record the occurance of elements in the sliding window
        left=0
        right=n-1
        frequency = defaultdict(int)
        for char in s[left:right+1]:
            frequency[char]+=1
        if frequency==target_dict:
            result.append(left)

        # slide the window from the left to the right
        while right<m-1:
            left+=1
            right+=1
            frequency[s[left-1]]-=1
            frequency[s[right]]+=1
            flag=True

            #check if the the records equal or not
            for key in target_dict.keys():
                if target_dict[key]!=frequency[key]:
                    flag=False

            # the two records are the same
            if flag:
                result.append(left)



        return result


    def findAnagrams_Time_Out_Method(self, s: str, p: str) -> List[int]:
        def permutation(self, p: str) -> List[str]:
            n = len(p)
            if n == 0:
                return ['']
            result = []
            for i in range(n):
                result += [p[i] + item for item in self.permutation(p[0:i] + p[i + 1:])]
            return result

        m=len(s)
        n=len(p)
        if m<n:
            return []
        permutation=permutation(p)
        permutation=set(permutation)
        print(permutation)
        result=[]
        for i in range(m-n+1):
            if s[i:i+n] in permutation:
                result.append(i)
        return result

if __name__=='__main__':
    print(Solution().findAnagrams(
        "aaaaaaaaaa",
        "aa"
    ))

