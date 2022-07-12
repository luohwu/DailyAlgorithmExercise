# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

from typing import List


class Solution:
    # important: this problem requires O(1) space
    # for each number, use binary_search to find target-number
    # Time: O(nlogn)
    # Space: O(1)
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        def binary_search(nums: List[int], target):
            left = 0
            right = len(nums)
            while left < right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    return mid
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid
            return -1

        n = len(numbers)
        for i in range(n):
            cur = numbers[i]
            complement = target - cur
            complement_idx = binary_search(numbers[i + 1:], target=complement)
            if complement_idx != -1:
                return [i+1, i+1+complement_idx+1]


if __name__=='__main__':
    print(Solution().twoSum(
        numbers = [2,7,11,15], target = 9
    ))
