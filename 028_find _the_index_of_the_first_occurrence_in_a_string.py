# https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/
# Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

# For each possible starting position in haystack, compare characters with needle and stop if a mismatch occurs.
# Time complexity: O(n^2)
# Space complexity: O(1)

class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        for i in range(len(haystack) - len(needle) + 1):
            for j in range(len(needle)):
                if haystack[i + j] != needle[j]:
                    break
            else:    # the for/else loop reaches here if no break occurs
                return i
        return -1