# flake8: noqa
# pylint: skip-file
# type: ignore
#
import unittest
from typing import List


class Solution:
    """
    Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
    You may assume that each input would have exactly one solution, and you may not use the same element twice.
    You can return the answer in any order.

    Example 1:
    Input: nums = [2,7,11,15], target = 9
    Output: [0,1]
    Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

    Example 2:
    Input: nums = [3,2,4], target = 6
    Output: [1,2]

    Example 3:
    Input: nums = [3,3], target = 6
    Output: [0,1]

    Constraints:
    2 <= nums.length <= 104
    -109 <= nums[i] <= 109
    -109 <= target <= 109
    Only one valid answer exists.

    Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?
    """
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        seen = {}

        for index in range(len(nums)):
            value = nums[index]
            remainder = target - value

            if remainder in seen:
                return [index, seen[remainder]]

            seen[value] = index

        return []


class Test(unittest.TestCase):
    def test(self):
        solution = Solution()

        result = solution.twoSum([2,7,11,15], 9)
        self.assertTrue(result in ([0,1], [1,0]))

        result = solution.twoSum([3,2,4], 6)
        self.assertTrue(result in ([1,2], [2,1]))

        result = solution.twoSum([3,3], 6)
        self.assertTrue(result in ([0,1], [1,0]))


if __name__ == '__main__':
    unittest.main()
