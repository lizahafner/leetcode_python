# https://leetcode.com/problems/plus-one/
# You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer.
# The digits are ordered from most significant to least significant in left-to-right order.
# The large integer does not contain any leading 0's.

# Start from the least significant digit, replace with zeros
# until the first non-9 digit is found, which is incremented.
# Time complexity: O(n)
# Space complexity: O(1)

class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        i = len(digits)-1
        while i >= 0 and digits[i] == 9:
            digits[i] = 0
            i -= 1
        if i == -1:
            return [1] + digits
        return digits[:i] + [digits[i]+1] + digits[i+1:]