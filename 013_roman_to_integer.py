# https://leetcode.com/problems/roman-to-integer/
# Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
# Convert a Roman numeral to an integer.
# Input is guaranteed to be between 1 and 3999.

# Traverse the string and check if the current and next characters
# form a valid Roman numeral with two symbols.
# If so, add its value to the result. Otherwise, the current single
# character must correspond to a valid numeral, which is added to the result.
# Time complexity: O(n)
# Space complexity: O(1)

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        doubles = {'CM': 900, 'CD': 400, 'XC': 90, 'XL': 40, 'IX': 9, 'IV': 4}
        singles = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
        integer = 0
        i = 0
        while i < len(s):
            if i < len(s) - 1 and s[i:i + 2] in doubles:    # check if two characters form a valid numeral
                integer += doubles[s[i:i + 2]]
                i += 2
            else:
                integer += singles[s[i]]                
                i += 1
        return integer