# https://leetcode.com/problems/linked-list-cycle/
# Given head, the head of a linked list, determine if the linked list has a cycle in it.
# There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. # # Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

# Return true if there is a cycle in the linked list. Otherwise, return false.

# Increment the fast pointer by 2 nodes and the slow pointer by 1 node at each time step.
# If there is a loop, the fast pointer will catch up with the slow pointer.
# Otherwise, the fast pointer will reach the end.
# Time complexity: O(n)
# Space complexity: O(1)

# Definition for singly-linked list.
class ListNode(object):
    def init(self, x):
        self.val = x
        self.next = None
class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        fast, slow = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if fast == slow:
                return True
        return False