# https://leetcode.com/problems/pascals-triangle/
# Given an integer numRows, return the first numRows of Pascal's triangle.
# In Pascal's triangle, each number is the sum of the two numbers directly above it as shown.

# The next row is the sum of consecutive pairs of items from the previous row.
# Time complexity: O(n^2)
# Space complexity: O(n^2)

class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0:
            return []
        pascal = [[1]]
        for i in range(1, numRows):
            pascal.append([1])
            for num1, num2 in zip(pascal[-2][:-1], pascal[-2][1:]):
                pascal[-1].append(num1 + num2)
            pascal[-1].append(1)
        return pascal