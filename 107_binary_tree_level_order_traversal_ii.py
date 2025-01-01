# https://leetcode.com/problems/binary-tree-level-order-traversal-ii/
# Given the root of a binary tree, return the bottom-up level order traversal of its nodes' values.
# (i.e., from left to right, level by level from leaf to root).

# Perform an inorder traversal, track depth, and append
# node values to the corresponding sublist. Reverse
# the result before returning.
# Time complexity: O(n)
# Space complexity: O(n)

# Definition for a binary tree node.
class TreeNode(object):
    def init(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        traversal = []
        self.inorder(root, 0, traversal)
        return traversal[::-1]
    def inorder(self, node, depth, traversal):
        if not node:
            return
        if len(traversal) == depth:
            traversal.append([])
        self.inorder(node.left, depth+1, traversal)
        traversal[depth].append(node.val)
        self.inorder(node.right, depth+1, traversal)