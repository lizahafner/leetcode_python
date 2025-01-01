# https://leetcode.com/problems/remove-duplicates-from-sorted-array
# Given an integer array nums sorted in non-decreasing order,
# remove the duplicates in-place such that each unique element appears only once.
# The relative order of the elements should be kept the same. Then return the number of unique elements in nums.

# Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:
# Change the array nums such that the first k elements of nums contain the unique elements
# in the order they were present in nums initially. The remaining elements of nums are not important as well as the size of nums.
# Return k.

# Remove duplicates from a sorted array in place.
# Time complexity: O(n)
# Space complexity: O(1)

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        next_new = 0    # index to place the next unique number
        for i in range(len(nums)):
            if i == 0 or nums[i] != nums[i - 1]:    # if it's the first or a new unique number
                nums[next_new] = nums[i]
                next_new += 1
        return next_new