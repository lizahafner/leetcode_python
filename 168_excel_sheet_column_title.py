# https://leetcode.com/problems/excel-sheet-column-title/
# Given an integer columnNumber, return its corresponding column title as it appears in an Excel sheet.
# For example: A -> 1, B -> 2, C -> 3 ... Z -> 26, AA -> 27, AB -> 28 ...

# Generate characters starting with least significant by calculating remainder of division by 26.
# Time complexity: O(log n)
# Space complexity: O(log n)

from collections import deque
class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        column = deque()    # faster than list for appendleft()
        while n > 0:
            n, output = divmod(n-1, 26)
            column.appendleft(output)
        return "".join([chr(i+ord('A')) for i in column])
