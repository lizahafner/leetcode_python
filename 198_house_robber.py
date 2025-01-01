# https://leetcode.com/problems/house-robber/
# You are a professional robber planning to rob houses along a street.
# Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have
# security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

# Given an integer array nums representing the amount of money of each house,
# return the maximum amount of money you can rob tonight without alerting the police.

# Either skip the current house and take the maximum from all previous houses,
# or rob the current house, skip the previous one, and take the maximum of the rest.
# Time complexity: O(n)
# Space complexity: O(1)

class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        loot, prev = nums[0], 0     # max from robbing this and previous adjacent houses
        for num in nums[1:]:
            loot, prev = max(num + prev, loot), loot
        return loot