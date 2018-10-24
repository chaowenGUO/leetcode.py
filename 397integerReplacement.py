class Solution:
    def integerReplacement(self, n):
        """
        :type n: int
        :rtype: int
        """
        result = 0
        while n > 1:
            if n & 1 == 0: n //= 2
            elif n & 3 == 1 or n == 3: n -= 1
            else: n += 1
            result += 1
        return result
