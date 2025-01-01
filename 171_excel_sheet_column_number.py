# https://leetcode.com/problems/excel-sheet-column-number/
# Given a string columnTitle that represents the column title as appears in an Excel sheet, return its corresponding column number.
# For example: A -> 1, B -> 2, C -> 3 ... Z -> 26, AA -> 27, AB -> 28 ...

# For each char, multiply the previous result by 26 and add the value of the char.
# Time complexity: O(n)
# Space complexity: O(n)

class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = 0
        for c in s:
            result = result*26 + ord(c) - ord('A') + 1
        return result