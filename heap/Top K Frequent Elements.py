# # https://leetcode.com/problems/top-k-frequent-elements/
#
# import heapq
# from typing import List,Optional
#
#
# class HeapNode:
#     def __init__(self,number,freq):
#         self.number=number
#         self.frequency=freq
#
#     def __repr__(self):
#         return f'Node value: {self.frequency}'
#
#     def __lt__(self, other):
#         self.frequency<=other.frequency
#
#
# class Solution:
#     def topKFrequent(self, nums: List[int], k: int) -> List[int]:
#         table=dict()
#         for num in nums:
#             if num in table.keys():
#                 table[num]+=1
#             else:
#                 table[num]=1
#         heap=[]
#         for number,freq in table.items():
#             heap.append(HeapNode(number=number,freq=freq))
#         heapq.heapify(heap)
#         result_nodes=heapq.nlargest(k,heap)
#         res=[]
#         for node in result_nodes:
#             res.append(node.number)
#         return res
#
#
# if __name__=='__main__':
#     print(Solution().topKFrequent(
#
#         [3, 0, 1, 0],
#     1
#     ))
