# https://leetcode.com/problems/valid-parentheses/
# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
# An input string is valid if:
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.

# Use a stack to keep track of opening brackets. For each closing bracket,
# check if it matches the last opening bracket by popping the top of the stack.
# Time complexity: O(n)
# Space complexity: O(n)

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        match = {'(': ')', '[': ']', '{': '}'}
        for c in s:
            if c in match:
                stack.append(c)
            else:
                # if the stack is empty or the top of the stack doesn't match the closing bracket, return False
                if not stack or match[stack.pop()] != c:
                    return False
        return not stack