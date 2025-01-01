# https://leetcode.com/problems/count-and-say/
# The count-and-say sequence is a sequence of digit strings defined by the recursive formula:
# countAndSay(1) = "1"
# countAndSay(n) is the run-length encoding of countAndSay(n - 1).

# Run-length encoding (RLE) is a string compression method that works by replacing consecutive identical characters (repeated 2 or more times) # with the concatenation of the character and the number marking the count of the characters (length of the run).
# For example, to compress the string "3322251" we replace "33" with "23", replace "222" with "32".
# Replace "5" with "15" and replace "1" with "11". Thus the compressed string becomes "23321511".
# Given a positive integer n, return the nth element of the count-and-say sequence.

# Iterate through the previous sequence. When a different number is found, append [1, num] to the new sequence.
# Increment the count when the same number repeats.
# Time complexity: O(2^n), as the sequence can double in length at worst.
# Space complexity: O(2^n)

class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        sequence = [1]
        for _ in range(n-1):
            next = []
            for num in sequence:
                if not next or next[-1] != num:
                    next += [1, num]
                else:
                    next[-2] += 1
            sequence = next
        return "".join(map(str, sequence))