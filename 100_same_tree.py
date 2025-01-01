# https://leetcode.com/problems/same-tree/
# Given the roots of two binary trees p and q, write a function to check if they are the same or not.
# Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

# Traverse both trees, ensuring nodes are in the same positions and values are identical. Can use preorder, inorder, or postorder traversal.
# Time complexity: O(min(m, n))
# Space complexity: O(min(m, n)), or O(log n) for balanced trees.

# Definition for a binary tree node.
class TreeNode(object):
    def init(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val != q.val:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)