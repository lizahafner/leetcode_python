# https://leetcode.com/problems/reverse-integer/
# Given a signed 32-bit integer x, return x with its digits reversed.
# If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
# Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

# Reverse digits of an integer.
# Example1: x = 123, return 321
# Example2: x = -123, return -321

# Continuously multiply the current result by 10 and add the last digit of x.
# Time complexity: O(n), where n is the number of digits in x.
# Space complexity: O(n), as the output will have the same number of digits as the input.

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        negative = x < 0    # check if the number is negative, then convert to positive
        x = abs(x)
        reversed = 0
        while x != 0:
            reversed = reversed * 10 + x % 10    # shift digits and add the last one from x
            x //= 10    # remove the last digit from x
        if reversed > 2**31 - 1:    # ensure the result fits within the 32-bit integer range (specific to LeetCode)
            return 0
        return reversed if not negative else -reversed    # restore the negative sign if needed