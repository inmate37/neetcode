# flake8: noqa
# pylint: skip-file
# type: ignore
#
import unittest


class Solution:
    """
    Given two strings s and t, return true if t is an anagram of s, and false otherwise.
    An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

    Example 1:
    Input: s = "anagram", t = "nagaram"
    Output: true

    Example 2:
    Input: s = "rat", t = "car"
    Output: false

    Constraints:
    1 <= s.length, t.length <= 5 * 104
    s and t consist of lowercase English letters.

    Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?
    """
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        seen = {}

        for i in s:
            if i not in seen:
                seen[i] = 1
            else:
                seen[i] += 1

        seen_t = {}

        for i in t:
            if i not in seen:
                return False

            if i not in seen_t:
                seen_t[i] = 1
            else:
                seen_t[i] += 1

        return seen == seen_t


class Test(unittest.TestCase):
    def test(self):
        solution = Solution()

        result = solution.isAnagram('anagram', 'nagaram')
        self.assertEqual(result, True)

        result = solution.isAnagram('rat', 'car')
        self.assertEqual(result, False)


if __name__ == '__main__':
    unittest.main()
