class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """

        if n < 5:
            return self.climb_stairs(n)
        else:
            j = self.climb_stairs(4)
            k = self.climb_stairs(5)
            nxt = j + k

            i = 0
            while n - 5 >= i:
                nxt = j + k
                k = j
                j = nxt
                i += 1
            return nxt

    def climb_stairs(self, n, step=0) -> int:
        """
        Returns the total number of ways that the remaining steps can be climbed.
        """

        if step == n:
            return 0
        elif step == n-1:
            return 0
        else:
            return self.climb_stairs(n, step+1) + self.climb_stairs(n, step+2) + 1
