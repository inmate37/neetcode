# flake8: noqa
# pylint: skip-file
# type: ignore
#
import unittest
from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        seen = {}

        for num in nums:
            if num in seen:
                return True

            seen[num] = None

        return False


class Test(unittest.TestCase):
    def run(self):
        solution = Solution()

        result = solution.containsDuplicate([1,2,3,1])
        self.assertEqual(result, True)

        result = solution.containsDuplicate([1,2,3,4])
        self.assertEqual(result, False)

        result = solution.containsDuplicate([1,1,1,3,3,4,3,2,4,2])
        self.assertEqual(result, True)


if __name__ == '__main__':
    unittest.main()


# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
#
#
# Example 1:
# Input: nums = [1,2,3,1]
# Output: true
#
# Example 2:
# Input: nums = [1,2,3,4]
# Output: false
#
# Example 3:
# Input: nums = [1,1,1,3,3,4,3,2,4,2]
# Output: true
#
#
# Constraints:
# 1 <= nums.length <= 105
# -109 <= nums[i] <= 109
