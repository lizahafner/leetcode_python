# https://leetcode.com/problems/palindrome-number/
# Given an integer x, return true if x is a palindrome and false otherwise.

# Check if an integer is a palindrome without using extra space.
# Compare the first and last digits, moving towards the center.
# Time complexity: O(n)
# Space complexity: O(1)

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        s = str(x)
        left, right = 0, len(s) - 1
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True