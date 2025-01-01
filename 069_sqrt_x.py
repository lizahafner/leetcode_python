# https://leetcode.com/problems/sqrtx/
# Given a non-negative integer x, return the square root of x rounded down to the nearest integer.
# The returned integer should be non-negative as well.
# You must not use any built-in exponent function or operator.
# For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.

# Implement int sqrt(int x).
# Compute and return the square root of x.

# Newton's method. Start with an initial guess of x. Iteratively update
# the guess to be the average of the previous guess and x // guess.
# Since the guess is too high, x // guess is too low.
# Terminate when guess^2 <= x.
# Time complexity: O((log x)^3) - log x for the number of iterations,
# log x for multiplication, and log x for division.
# Space complexity: O(1)

class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        guess = x
        while guess * guess > x:
            guess = (guess + x // guess) // 2
        return guess