# https://leetcode.com/problems/rotate-array/
# Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

# Reverse the entire array, then reverse the first k elements and the last n-k elements.
# Alternatively, split after n-k elements and swap the slices.
# Time complexity: O(n)
# Space complexity: O(1)

class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        k %= len(nums)
        nums.reverse()
        nums[:k] = reversed(nums[:k])
        nums[k:] = reversed(nums[k:])
class Solution2(object):
    def rotate(self, nums, k):
        n = len(nums)
        k %= n
        nums[:] = nums[n-k:] + nums[:n-k]