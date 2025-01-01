# https://leetcode.com/problems/add-binary/
# Given two binary strings a and b, return their sum as a binary string.

# Start with the least significant digits, add the digits together. 
# Reverse the result string at the end.
# Time complexity: O(max(m, n))
# Space complexity: O(1)

class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        result = []
        carry = 0
        i = len(a)-1
        j = len(b)-1
        while carry or i >= 0 or j >= 0:
            total = carry
            if i >= 0:
                total += int(a[i])
                i -= 1
            if j >= 0:
                total += int(b[j])
                j -= 1
            result.append(str(total % 2))
            carry = total // 2
        return "".join(result[::-1])