# https://leetcode.com/problems/majority-element/
# Given an array nums of size n, return the majority element.
# The majority element is the element that appears more than ⌊n / 2⌋ times.
# You may assume that the majority element always exists in the array.

# When the count is zero, the next element becomes the candidate.
# When an element matches the candidate, increment the count; otherwise, decrement it.
# Time complexity: O(n)
# Space complexity: O(1)

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count, candidate = 0, None
        for i, num in enumerate(nums):
            if count == 0:
                candidate = num

            if candidate == num:
                count += 1
            else:
                count -= 1
        return candidate
