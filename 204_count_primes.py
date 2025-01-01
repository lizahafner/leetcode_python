# https://leetcode.com/problems/count-primes/
# Given an integer n, return the number of prime numbers that are strictly less than n.

# Use the Sieve of Eratosthenes: assume all numbers are prime and eliminate those with factors.
# Time complexity: O(n^(3/2))
# Space complexity: O(n)

class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        sieve = [False, False] + [True for _ in range(n-2)]     # numbers 0 and 1 are not prime
        for i in range(2, int(n**0.5) + 1):     # stop at sqrt(j) since any non-prime j must have a factor ≤ sqrt(j).
            if sieve[i]:                        # i is prime
                sieve[i*i:n:i] = [False] * len(sieve[i*i:n:i])  # the list comprehension faster than loop
                                                                # start at i*i since i*(i-1) has already been eliminated
        return sum(sieve)

