class Solution:
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        import functools
        return functools.reduce(lambda catalan, _: catalan * 2 * (2 * _ + 1) // (_ + 2), range(n), 1)
