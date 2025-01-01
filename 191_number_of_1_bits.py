# https://leetcode.com/problems/number-of-1-bits/
# Given a positive integer n, write a function that returns the number of set bitsin its binary representation
# Also known as the Hamming weight.

# Convert the number to a string and count the occurrences of '1' characters.
# Time complexity: O(log n)
# Space complexity: O(log n)

class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        return sum(c == "1" for c in bin(n)[2:])
