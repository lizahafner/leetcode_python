# https://leetcode.com/problems/maximum-subarray/
# The count-and-say sequence is a sequence of digit strings defined by the recursive formula:
# Given an integer array nums, find the subarray with the largest sum, and return its sum.

# For each number, calculate the maximum subarray sum ending with that number:
# either the number alone (if the previous sum was negative) or the number plus the previous sum (if it was positive).
# Time complexity: O(n)
# Space complexity: O(1)

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        overall_max = float('-inf')
        max_ending_here = 0
        for num in nums:
            if max_ending_here > 0:
                max_ending_here += num
            else:
                max_ending_here = num
            overall_max = max(overall_max, max_ending_here)
        return overall_max