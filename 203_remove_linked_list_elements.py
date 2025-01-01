# https://leetcode.com/problems/remove-linked-list-elements/
# Given the head of a linked list and an integer val, remove all the nodes of the linked list
# that has Node.val == val, and return the new head.

# Traverse the list, removing nodes with the specified value.
# Time complexity: O(n)
# Space complexity: O(1)

# Definition for singly-linked list.
class ListNode(object):
    def init(self, x):
        self.val = x
        self.next = None
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        dummy = prev = ListNode(None)   # dummy in case head is deleted
        dummy.next = head
        while head:
            if head.val == val:
                prev.next, head.next, head = head.next, None, head.next
            else:
                prev, head = head, head.next
        return dummy.next
