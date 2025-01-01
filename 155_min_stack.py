# https://leetcode.com/problems/min-stack/
# Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

# Implement the MinStack class:
# MinStack() initializes the stack object.
# void push(int val) pushes the element val onto the stack.
# void pop() removes the element on the top of the stack.
# int top() gets the top element of the stack.
# int getMin() retrieves the minimum element in the stack.
# You must implement a solution with O(1) time complexity for each function.

# The main stack contains all items, while the min stack contains
# items that are less than or equal to the previous minimum.
# Note: No error handling for empty stack is required.
# Time complexity: O(1)
# Space complexity: O(n)

class MinStack(object):
    def init(self):
        """
        initialize your data structure here.
        """
        self.main = []
        self.mins = []
    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.main.append(x)
        if not self.mins or x <= self.mins[-1]:
            self.mins.append(x)
    def pop(self):
        """
        :rtype: void
        """
        item = self.main.pop()
        if item == self.mins[-1]:
            self.mins.pop()
    def top(self):
        """
        :rtype: int
        """
        return self.main[-1]
    def getMin(self):
        """
        :rtype: int
        """
        return self.mins[-1]
