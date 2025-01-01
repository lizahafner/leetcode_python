# https://leetcode.com/problems/factorial-trailing-zeroes/
# Given an integer n, return the number of trailing zeroes in n!.
# Note that n! = n * (n - 1) * (n - 2) * ... * 3 * 2 * 1.

# Every trailing zero is produced by a factor of 5 (since there are many more factors of 2 that together form trailing zeroes).
# Count the numbers in 1..n divisible by 5, then those divisible by 25 (which contribute an extra factor of 5), then 125, and so on...
# Time complexity: O(log n)
# Space complexity: O(1)

class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        zeroes = 0
        power_of_5 = 5
        while power_of_5 <= n:
            zeroes += n // power_of_5
            power_of_5 *= 5
        return zeroes