# https://leetcode.com/problems/time-based-key-value-store/

from collections import defaultdict
class TimeMap:

    def __init__(self):
        # defaultdict is better than dict()
        self.table=defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.table[key].append([timestamp,value])

    def get(self, key: str, timestamp: int) -> str:
        # just binary search
        left=0
        right=len(self.table[key])
        while left<right:
            mid=(left+right)//2
            if timestamp<self.table[key][mid][0]:
                right=mid
            else:
                left=mid+1
        if right==0:
            return ""
        else:
            # note that it's left-1
            return self.table[key][left-1][1]





# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)


