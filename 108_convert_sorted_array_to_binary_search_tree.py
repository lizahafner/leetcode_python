# https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/
# Given an integer array nums where the elements are sorted in ascending order, convert it to a height-balanced binary search tree.

# The middle element is the root, recursively form the left and right subtrees.
# Time complexity: O(n)
# Space complexity: O(n)

# Definition for a binary tree node.
class TreeNode(object):
    def init(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        return self.convert(nums, 0, len(nums)-1)
    def convert(self, nums, left, right):
        if left > right:
            return None
        mid = (left + right) // 2
        root = TreeNode(nums[mid])
        root.left = self.convert(nums, left, mid-1)
        root.right = self.convert(nums, mid+1, right)
        return root