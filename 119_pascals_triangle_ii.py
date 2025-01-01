# https://leetcode.com/problems/pascals-triangle-ii/
# Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.
# In Pascal's triangle, each number is the sum of the two numbers directly above it as shown.

# The next row is the sum of consecutive pairs from the previous row.
# Time complexity: O(n^2)
# Space complexity: O(n)

class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        row = [1]
        for i in range(rowIndex):
            row = [1] + [row[i]+row[i+1] for i in range(len(row)-1)] + [1]
        return row