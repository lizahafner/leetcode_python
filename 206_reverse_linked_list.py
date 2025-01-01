# https://leetcode.com/problems/reverse-linked-list/
# Given the head of a singly linked list, reverse the list, and return the reversed list.

# Iteratively reverse the list. Alternatively, use recursion.
# Time complexity: O(n)
# Space complexity: O(1)

# Definition for the singly-linked list.
class ListNode(object):
    def init(self, x):
        self.val = x
        self.next = None
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        reversed = None
        while head:
            next = head.next
            head.next = reversed
            reversed = head
            head = next
        return reversed
