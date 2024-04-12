# flake8: noqa
# pylint: skip-file
# type: ignore
#
import unittest
from typing import List


class Solution:
    """
    Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
    The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
    You must write an algorithm that runs in O(n) time and without using the division operation.

    Example 1:
    Input: nums = [1,2,3,4]
    Output: [24,12,8,6]

    Example 2:
    Input: nums = [-1,1,0,-3,3]
    Output: [0,0,9,0,0]

    Constraints:
    2 <= nums.length <= 105
    -30 <= nums[i] <= 30
    The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

    Follow up: Can you solve the problem in O(1) extra space complexity? (The output array does not count as extra space for space complexity analysis.)
    """
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)  # 4
        store = [1] * n  # [1, 1, 1, 1]

        # Product of all elements on left
        left = 1
        for i in range(n):  # 0, 1, 2, 3
            store[i] *= left
            left *= nums[i]

        # Product of all elements on right
        right = 1
        for i in range(n-1, -1, -1):  # 3, 2, 1, 0
            store[i] *= right
            right *= nums[i]

        return store



class Test(unittest.TestCase):
    def test(self):
        solution = Solution()

        result = solution.productExceptSelf([1,2,3,4])
        self.assertEqual(result, [24,12,8,6])

        result = solution.productExceptSelf([-1,1,0,-3,3])
        self.assertEqual(result, [0,0,9,0,0])


if __name__ == '__main__':
    unittest.main()
