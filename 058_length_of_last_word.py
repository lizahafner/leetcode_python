# https://leetcode.com/problems/length-of-last-word/
# Given a string s consisting of words and spaces, return the length of the last word in the string.
# A word is a maximal substring consisting of non-space characters only.

# Start from the last character and decrement i.
# Set the end variable when a non-blank character is found.
# Return the next non-blank character.
# Time complexity: O(n)
# Space complexity: O(1)

class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        i = len(s) - 1
        end = -1
        while i >= 0:
            if s[i] == ' ' and end != -1:
                return end - i
            if s[i] != ' ' and end == -1:
                end = i
            i -= 1
        return end + 1 if end != -1 else 0