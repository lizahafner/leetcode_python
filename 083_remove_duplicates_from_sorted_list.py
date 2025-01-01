# https://leetcode.com/problems/remove-duplicates-from-sorted-list/
# Given the head of a sorted linked list, delete all duplicates such that each element appears only once.
# Return the linked list sorted as well.

# If the next node is the same as the current node, link the current node to node.next.next.
# Otherwise, move to the next node.
# Time complexity: O(n)
# Space complexity: O(1)

# Definition maked for singly-linked list.
class ListNode(object):
    def init(self, x):
        self.val = x
        self.next = None
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        node = head
        while node and node.next:
            if node.val == node.next.val:
                node.next = node.next.next
            else:
                node = node.next
        return head