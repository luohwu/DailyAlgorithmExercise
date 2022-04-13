# https://leetcode.com/problems/two-sum/

#Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        table = {}
        for i, item in enumerate(nums):
            complement = target - item
            if complement in table and not table[complement] == i:
                return [i, table[complement]]
            table[item] = i

