# https://leetcode.com/problems/isomorphic-strings/
# Given two strings s and t, determine if they are isomorphic.
# Two strings s and t are isomorphic if the characters in s can be replaced to get t.
# All occurrences of a character must be replaced with another character while preserving the order of characters.
# No two characters may map to the same character, but a character may map to itself.

# Store a mapping from characters in s to characters in t. If a character in s
# is already mapped, verify that the corresponding character in t is the same as before.
# Also, ensure that a new character in s is not mapped to a character in t that has already been mapped.
# Time complexity: O(n)
# Space complexity: O(n)

class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        s_to_t = {}
        t_mapped = set()
        for cs, ct in zip(s, t):
            if cs in s_to_t:
                if s_to_t[cs] != ct:
                    return False
            elif ct in t_mapped:
                return False
            s_to_t[cs] = ct
            t_mapped.add(ct)
        return True

