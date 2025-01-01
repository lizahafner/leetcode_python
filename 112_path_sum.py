# https://leetcode.com/problems/path-sum/
# Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path
# such that adding up all the values along the path equals targetSum.
# A leaf is a node with no children.

# Base cases: return False if there is no node, and True if it's a leaf node with
# the correct sum. Otherwise, subtract the node value and check if
# True is found in either subtree.
# Time complexity: O(n)
# Space complexity: O(n)

# Definition for a binary tree node.
class TreeNode(object):
    def init(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if not root:
            return False
        sum -= root.val
        if sum == 0 and not root.left and not root.right:    # that is a leaf node
            return True
        return self.hasPathSum(root.left, sum) or self.hasPathSum(root.right, sum)