# https://leetcode.com/problems/longest-common-prefix/
# Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string "".

# Sort the strings and find the longest common prefix between the first and last strings in the sorted list,
# as these two are the most different.
# Alternatively, all strings could be stored in a trie
# and the common prefix would be determined by finding the first node with more than one child.
# Time complexity: O(k * n log n), where k is the length of the longest string and n is the number of strings.
# Space complexity: O(1)

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ''
        strs.sort()
        first = strs[0]
        last = strs[-1]

        i = 0
        while i < len(first) and i < len(last) and first[i] == last[i]:
            i += 1
        return first[:i]